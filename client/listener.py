#!/usr/bin/env python
# ------------------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------
 
import time
import sys
import os
import stomp

user = os.getenv("ACTIVEMQ_USER") or "admin"
password = os.getenv("ACTIVEMQ_PASSWORD") or "admin"
host = os.getenv("ACTIVEMQ_HOST") or "192.168.1.3"
port = os.getenv("ACTIVEMQ_PORT") or 61613
destination = sys.argv[1:2] or ["/topic/event"]
destination = destination[0]

print(user,password,host,port)

def connect_and_subscribe(conn):
  conn.connect(login=user,passcode=password)
  conn.subscribe(destination=destination, id=1, ack='auto')


class MyListener(object):
  
  def __init__(self, conn):
    self.conn = conn
    self.count = 0
    self.start = time.time()
  
  def on_error(self, frame):
        print('received an error "%s"' % frame.body)

  def on_message(self, frame):
      print('received a message "%s"' % frame.body)
      for x in range(10):
          print(x)
          time.sleep(1)
      print('processed message')

  def on_disconnected(self):
      print('disconnected')
      connect_and_subscribe(self.conn)

conn = stomp.Connection(host_and_ports = [(host, port)])
conn.set_listener('', MyListener(conn))
connect_and_subscribe(conn)
print("Waiting for messages...")
while 1: 
  time.sleep(10) 
