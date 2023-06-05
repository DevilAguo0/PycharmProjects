1.	from sqlalchemy import Column, Integer,String, create_engine,and_
2.	from sqlalchemy.orm import sessionmaker
3.	from sqlalchemy.ext.declarative import declarative_base
4.
5.	# 初始化数据库连接:
6.	engine = create_engine('mysql+pymysql://root:123456@localhost:3306/test_sqlalchemy',echo=False)
7.
8.	# 创建连接池DBSession类型:
9.DBSession = sessionmaker(bind=engine)
10.
11.	# 创建对象的基类:
12.Base = declarative_base()
13.Base.metadata.create_all(engine)
14.
15.	# 定义User对象:
16.	class User(Base):
17.	    # 表的名字:
18.	    __tablename__ = 'user'
19.
20.	    # 表的结构:
21.	    id = Column(String(20), primary_key=True)
22.	    name = Column(String(20))
23.
24.
25.
26.	class Account_Table(Base):                      #账号表
27.	    __tablename__ = 'account_table'
28.
29.	    User = Column(String(20), primary_key=True) #账号
30.	    Password = Column(String(30),nullable=False) #密码
31.	    ID_Number = Column(String(100))             #身份证号码或者护照号码或者其他ID码
32.	    Category = Column(String(10))               #账号类别
33.
34.
35.	#-------------管理员操作--------------
36.	    #添加账号
37.	    def Insert_Account(n_user,n_password,n_id,n_category):
38.	        session = DBSession()
39.	        new_Accout = Account_Table(User = n_user,Password = n_password,
40.	                                   ID_Number = n_id,
41.	                                   Category = n_category)
42.	        session.add(new_Accout)
43.	        try:
44.	            session.commit()
45.	        except Exception as e:
46.	            session.rollback()
47.
48.	        session.close()
49.
50.	    #删除账号
51.	    def Delete_Account(del_user):
52.	        session = DBSession()
53.
54.	        result = session.query(Account_Table).filter(Account_Table.User == del_user).delete()
55.	        session.commit()
56.	        session.close()
57.
58.
59.	    #查看账号
60.	    def Query_Account(cate):
61.	        session = DBSession()
62.	        result = session.query(Account_Table).filter(Account_Table.Category == cate)
63.	        try:
64.	            session.commit()
65.	            return result
66.
67.	        except Exception as e:
68.	            session.rollback()
69.
70.	        session.close()
71.	    def Query_Cate(q_user):
72.	        session = DBSession()
73.
74.
75.	        try:
76.	            result = session.query(Account_Table).filter(Account_Table.User == q_user).one()
77.	            session.commit()
78.	            return result.Category
79.
80.	        except Exception as e:
81.	            session.rollback()
82.
83.
84.	    #修改账号
85.
86.	#--------
87.
88.	class Passenger_Table(Base):                        #乘客信息表
89.	    __tablename__ = 'passenger_table'
90.
91.
92.	    Name = Column(String(20))                   #1乘客姓名
93.	    Sex = Column(String(10))                    #2性别
94.	    Workplace = Column(String(50))              #3工作单位
95.
96.	    ID_Card_Number = Column(String(100),primary_key=True)       #4乘客身份证号
97.
98.	    travel_time = Column(String(20))                #5旅行出发时间
99.	    place_travel_start = Column(String(10))         #6旅行始发地
100.	    place_travel_end = Column(String(10))           #7旅行目的地
101.	    requirement_berths = Column(String(50))         #8舱位要求
102.
103.
104.
105.	    Flight_No = Column(String(20))                     #9航班号码
106.	    Travel_agency_No = Column(String(20))              #10旅行社号码
107.	    Order_NO = Column(String(20))                      #11订单号码
108.
109.	#-------------旅客操作-------------------------------------
110.	    #添加个人信息
111.	    def Insert_Passenger(n_Name,n_Sex,n_Workplace,n_ID_Card_Number,n_travel_time,n_place_travel_start,n_place_travel_end,n_requirement_berths,n_Flight_No,n_Travel_agency_No,n_Order_NO):
112.	        session = DBSession()
113.	        new_Passenger = Passenger_Table(Name = n_Name,
114.	                                        Sex = n_Sex,
115.	                                        Workplace = n_Workplace,
116.	                                        ID_Card_Number = n_ID_Card_Number,
117.	                                        travel_time = n_travel_time,
118.	                                        place_travel_start = n_place_travel_start,
119.	                                        place_travel_end = n_place_travel_end,
120.	                                        requirement_berths = n_requirement_berths,
121.	                                        Flight_No = n_Flight_No,
122.	                                        Travel_agency_No = n_Travel_agency_No,
123.	                                        Order_NO = n_Order_NO)
124.
125.	        session.add(new_Passenger)
126.	        try:
127.	            session.commit()
128.	        except Exception as e:
129.	            session.rollback()
130.
131.	        session.close()
132.
133.
134.	    #删除个人信息
135.	    def Delete_Passenger(del_ID_Card_Number):
136.	        session = DBSession()
137.
138.	        result = session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == del_ID_Card_Number).delete()
139.
140.	        session.commit()
141.	        session.close()
142.
143.	    #修改个人信息
144.	    def Update_Passenger(ID,Pos,Update_value):
145.	        session = DBSession()
146.
147.	        if Update_value != '':
148.	            if Pos == 0:
149.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.Name:Update_value})
150.	            elif Pos == 1:
151.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.Sex:Update_value})
152.	            elif Pos == 2:
153.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.Workplace:Update_value})
154.	            elif Pos == 3:
155.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.ID_Card_Number:Update_value})
156.	            elif Pos == 4:
157.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.travel_time:Update_value})
158.	            elif Pos == 5:
159.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.place_travel_start:Update_value})
160.	            elif Pos == 6:
161.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.place_travel_end:Update_value})
162.	            elif Pos == 7:
163.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.requirement_berths:Update_value})
164.	            elif Pos == 8:
165.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.Flight_No:Update_value})
166.	            elif Pos == 9:
167.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.Travel_agency_No:Update_value})
168.	            elif Pos == 10:
169.	                session.query(Passenger_Table).filter(Passenger_Table.ID_Card_Number == ID).update({Passenger_Table.Order_NO:Update_value})
170.	            else:
171.	                print("POS Err")
172.	        else :
173.	            print('Update_value: NULL')
174.
175.	        session.commit()
176.	        session.close()
177.
178.	    #查看对于旅行社的旅客信息
179.	    def Query_Passenger(T_No):
180.	        session = DBSession()
181.	        result = session.query(Passenger_Table).filter(Passenger_Table.Travel_agency_No == T_No)
182.	        try:
183.	            session.commit()
184.	            return result
185.
186.	        except Exception as e:
187.	            session.rollback()
188.
189.	        session.close()
190.
191.	#--------------------------------------
192.
193.
194.	class Airline_Company_Table(Base):              #航空公司表
195.	    __tablename__ = 'airline_company_table'
196.
197.	    No = Column(String(100),primary_key = True)
198.	    Name = Column(String(20))
199.
200.
201.	#添加航公司的名字和号码
202.	    def Insert_Company(n_No,n_Name):
203.	        session = DBSession()
204.
205.	        new_Company = Airline_Company_Table(No = n_No,
206.	                                            Name = n_Name)
207.	        session.add(new_Company)
208.
209.	        session.commit()
210.	        session.close()
211.	#删除航空公司名字和号码
212.	    def Delete_Company(del_No):
213.	        session = DBSession()
214.
215.	        result = session.query(Airline_Company_Table).filter(Airline_Company_Table.No == del_No).delete()
216.
217.	        session.commit()
218.	        session.close()
219.	#删除账号查询的航空公司名字和号码
220.	    def Delete_Company_from_Account(del_user):
221.	        session = DBSession()
222.
223.	        Account_result = session.query(Account_Table).filter(Account_Table.User == del_user).one()
224.
225.	        AIN = Account_result.ID_Number
226.
227.	        result = session.query(Airline_Company_Table).filter(Airline_Company_Table.No == AIN).delete()
228.	        session.commit()
229.	        session.close()
230.
231.	#查看航空公司名字和号码
232.	    def Query_Company(que_No):
233.	        session = DBSession()
234.	        result = session.query(Airline_Company_Table).filter(Airline_Company_Table.No == que_No)
235.	        try:
236.	            session.commit()
237.	            return result
238.
239.
240.	        except Exception as e:
241.	            session.rollback()
242.
243.	        session.close()
244.
245.	#------------------------------------
246.
247.
248.	class Travel_Agency_Table(Base):                #旅行社表
249.	    __tablename__ = 'travel_agency_table'
250.
251.	    No = Column(String(100),primary_key = True)
252.	    Name = Column(String(20))
253.
254.	#添加旅行社的号码
255.	    def Insert_Travel_Agency(n_No,n_Name):
256.	        session = DBSession()
257.
258.	        new_Travel_Agency = Travel_Agency_Table(No = n_No,
259.	                                                Name = n_Name)
260.	        session.add(new_Travel_Agency)
261.
262.	        session.commit()
263.	        session.close()
264.	#删除旅行社名字和号码
265.	    def Delete_Travel_Agency(del_No):
266.	        session = DBSession()
267.
268.	        result = session.query(Travel_Agency_Table).filter(Travel_Agency_Table.No == del_No).delete()
269.
270.	        session.commit()
271.	        session.close()
272.
273.	#删除账号查询的旅行社的名字
274.	    def Delete_Travel_Agency_from_Account(del_user):
275.	        session = DBSession()
276.
277.	        Account_result = session.query(Account_Table).filter(Account_Table.User == del_user).one()
278.
279.
280.	        AIN = Account_result.ID_Number
281.
282.	        result = session.query(Travel_Agency_Table).filter(Travel_Agency_Table.No == AIN).delete()
283.	        session.commit()
284.	        session.close()
285.
286.	#查看旅行社名字和号码
287.	    def Query_Travel_Agency(que_No):
288.	        session = DBSession()
289.	        result = session.query(Travel_Agency_Table).filter(Travel_Agency_Table.No == que_No)
290.	        try:
291.	            session.commit()
292.	            return result
293.
294.	        except Exception as e:
295.	            session.rollback()
296.
297.	        session.close()
298.
299.
300.
301.
302.	#---------------------------------
303.
304.
305.
306.
307.	class Flight_Information_Table(Base):               #航班信息表
308.	    __tablename__ = 'flight_information_table'
309.
310.	    Flight_no = Column(String(20),primary_key = True)  #1航班号码
311.	    air_company_No = Column(String(20))             #2航空公司号码
312.	    origin = Column(String(10))                     #3航班始发地
313.	    destination = Column(String(10))                #4航班目的地
314.
315.	    Aircraft_type = Column(String(10))              #5飞机型号
316.	    Num_P = Column(String(20))                         #6乘客数
317.	    #Seats = Column(Integer)                         #座位数
318.	    #remaining_seats = Column(Integer)               #剩余座位数
319.
320.	    scheduled_start_time = Column(String(20))         #7航班起飞时间
321.	    scheduled_arrival_time = Column(String(20))       #8航班预计到达时间
322.	    price = Column(String(50))                      #9航班价格
323.
324.
325.	#---------------------------航空公司操作---------------------------------
326.	    #添加航班
327.	    def Insert_Flight(n_Flight_no,n_air_company_No,n_origin,n_destination,n_Aircraft_type,n_Num_p,n_scheduled_start_time,n_scheduled_arrival_time,n_price):
328.	        session = DBSession()
329.
330.	        new_Flight = Flight_Information_Table(Flight_no = n_Flight_no,
331.	                                              air_company_No = n_air_company_No,
332.	                                              origin = n_origin,
333.	                                              destination = n_destination,
334.	                                              Aircraft_type = n_Aircraft_type,
335.	                                              Num_P = n_Num_p,
336.	                                              scheduled_start_time = n_scheduled_start_time,
337.	                                              scheduled_arrival_time = n_scheduled_arrival_time,
338.	                                              price = n_price)
339.
340.	        session.add(new_Flight)
341.
342.	        session.commit()
343.	        session.close()
344.
345.	    #删除航班
346.	    def Delete_Flight(del_Flight_no):
347.	        session = DBSession()
348.
349.	        result = session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == del_Flight_no).delete()
350.
351.	        print(result)
352.	        session.commit()
353.	        session.close()
354.
355.	    #查看航班信息
356.	    def Query_Flight(ACNO):
357.
358.	        session = DBSession()
359.	        result = session.query(Flight_Information_Table).filter(Flight_Information_Table.air_company_No == ACNO)
360.	        try:
361.	            session.commit()
362.	            return result
363.
364.
365.	        except Exception as e:
366.	            session.rollback()
367.
368.	        session.close()
369.
370.	    #修改航班信息
371.	    def Update_Flight(No,Pos,Update_value):
372.	        session = DBSession()
373.
374.	        if Update_value != '':
375.	            if Pos == 0:
376.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.Flight_no:Update_value})
377.	            elif Pos == 1:
378.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.air_company_No:Update_value})
379.	            elif Pos == 2:
380.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.origin:Update_value})
381.	            elif Pos == 3:
382.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.destination:Update_value})
383.	            elif Pos == 4:
384.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.Aircraft_type:Update_value})
385.	            elif Pos == 5:
386.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.Num_P:Update_value})
387.	            elif Pos == 6:
388.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.scheduled_start_time:Update_value})
389.	            elif Pos == 7:
390.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.scheduled_arrival_time:Update_value})
391.	            elif Pos == 8:
392.	                session.query(Flight_Information_Table).filter(Flight_Information_Table.Flight_no == No).update({Flight_Information_Table.price:Update_value})
393.	            else:
394.	                print("POS Err")
395.	        else :
396.	            print('Update_value: NULL')
397.
398.	        session.commit()
399.	        session.close()
400.
401.	#-----------------------------------------------------------------
402.
403.
404.
405.	class Order_information_table(Base):                #订单表
406.	    __tablename__ = 'order_information_table'
407.
408.	    Order_no = Column(String(20),primary_key = True)   #订单号码
409.	    ID_Card_Number = Column(String(100))            #身份证号码
410.	    Travel_agency_No = Column(String(20))              #旅行社号码
411.	    Flight_no = Column(String(20))                     #航班号码
412.	    price = Column(String(20))                        #价格
413.	    code_get_ticket = Column(String(20))               #取票码
414.	#---------订单操作-----------
415.	    #添加订单
416.	    def Insert_Order(n_Order_no,n_ID_Card_Number,n_Travel_agency_No,n_Flight_no,n_price,n_code_get_ticket):
417.	        session = DBSession()
418.
419.	        new_Order = Order_information_table(Order_no = n_Order_no,
420.	                                            ID_Card_Number = n_ID_Card_Number,
421.	                                            Travel_agency_No = n_Travel_agency_No,
422.	                                            Flight_no = n_Flight_no,
423.	                                            price = n_price,
424.	                                            code_get_ticket = n_code_get_ticket)
425.	        session.add(new_Order)
426.
427.	        session.commit()
428.	        session.close()
429.
430.	    #删除订单
431.	    def Delete_Order(del_Order_no):
432.	        session = DBSession()
433.
434.	        result = session.query(Order_information_table).filter(Order_information_table.Order_no == del_Order_no).delete()
435.
436.	        session.commit()
437.	        session.close()
438.
439.	    #查看订单
440.	    def Query_Order(O_NO):
441.
442.	        session = DBSession()
443.	        result = session.query(Order_information_table).filter(Order_information_table == O_NO)
444.	        try:
445.	            session.commit()
446.	            return result
447.
448.
449.	        except Exception as e:
450.	            session.rollback()
451.
452.	        session.close()
453.
454.
455.	    #修改订单
456.	    def Update_Order(No,Pos,Update_value):
457.	        session = DBSession()
458.
459.	        if Update_value != '':
460.	            if Pos == 0:
461.	                session.query(Order_information_table).filter(Order_information_table.Order_no == No).update({Order_information_table.Order_no:Update_value})
462.	            elif Pos == 1:
463.	                session.query(Order_information_table).filter(Order_information_table.Order_no == No).update({Order_information_table.ID_Card_Number:Update_value})
464.	            elif Pos == 2:
465.	                session.query(Order_information_table).filter(Order_information_table.Order_no == No).update({Order_information_table.Travel_agency_No:Update_value})
466.	            elif Pos == 3:
467.	                session.query(Order_information_table).filter(Order_information_table.Order_no == No).update({Order_information_table.Flight_no.Seats:Update_value})
468.	            elif Pos == 4:
469.	                session.query(Order_information_table).filter(Order_information_table.Order_no == No).update({Order_information_table.price:Update_value})
470.	            elif Pos == 5:
471.	                session.query(Order_information_table).filter(Order_information_table.Order_no == No).update({Order_information_table.code_get_ticket:Update_value})
472.	            else:
473.	                print("POS Err")
474.	        else :
475.	            print('Update_value: NULL')
476.
477.	        session.commit()
478.	        session.close()
479.	#---------------------------------------------
480.
481.
482.	#目前仅有显示功能，不可以返回值
483.	def Query_Table_ALL(table):
484.	    session = DBSession()
485.	    result = session.query(table).all()
486.	    try:
487.	        session.commit()
488.	        if table.__tablename__ == 'account_table':
489.	            return result
490.	        elif table.__tablename__ == 'passenger_table':
491.	            return result
492.	        elif table.__tablename__ == 'airline_company_table':
493.	            return result
494.	        elif table.__tablename__ == 'travel_agency_table':
495.	            return result
496.	        elif table.__tablename__ == 'flight_information_table':
497.	            return result
498.	        elif table.__tablename__ == 'order_information_table':
499.	            return result
500.
501.	    except Exception as e:
502.	        session.rollback()
503.
504.	    session.close()
505.
506.
507.
508.
509.
510.
511.
512.
513.
514.
515.
516.
517.
518.	#-------------------------
519.
520.
521.
522.	#旅客实操
523.	#Insert_Passenger('林肯郡','440813199945460125','张家口','北京',12,1128885)
524.	#Delete_Passenger('440813199945460125')
525.	#Update_Passenger('440813199945460125',0,'')
526.
527.	#航空公司实操
528.
529.	#订单实操
530.
531.
532.	Base.metadata.create_all(engine)
533.
534.	''''' 
535.	 
536.	#创建表 
537.	 
538.	 
539.	# 创建session对象: 
540.	session = DBSession() 
541.	# 创建新User对象: 
542.	new_user = User(id='5', name='Bob') 
543.	# 添加到session: 
544.	session.add(new_user) 
545.	# 提交即保存到数据库: 
546.	session.commit() 
547.	# 关闭session: 
548.	session.close() 
549.	 
550.	# 创建Session: 
551.	session = DBSession() 
552.	# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行: 
553.	#user = session.query(User).filter(User.id=='5').one() 
554.	user = session.query(User).all() 
555.	# 打印类型和对象的name属性: 
556.	print('type:', type(user)) 
557.	print(user) 
558.	 
559.	for each in user: 
560.	    print(each.id,each.name) 
561.	# 关闭Session: 
562.	session.close() 
563.	'''

