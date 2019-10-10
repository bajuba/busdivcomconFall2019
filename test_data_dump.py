from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from database import *

contest_list = []
events_list = []
schools_list = []
teachers_list = []
students_list = []
pictures_list = []

##add several Contests objects to a list of Contests##
contest_list.append(Contests("diam vel arcu.","2020-08-17 20:49:45","2019-08-08 23:25:28","2019-12-17 04:35:27","2019-07-02 16:56:46","2019-06-25 07:11:50",13,15,6,"Hashim Giles","Phasellus@elementumpurus.org","(779) 274-9705","euismod enim.","Arden Salas","semper rutrum.","Pellentesque.ultricies.dignissim@sagittisaugueeu.org"))
contest_list.append(Contests("Aenean massa. Integer","2019-08-20 00:19:39","2019-07-25 14:57:56","2019-07-05 13:37:35","2020-04-03 19:30:45","2019-07-05 10:14:08",12,15,5,"Yolanda Benton","nulla@sagittisDuisgravida.net","(818) 377-9564","dolor sit","Sybil Sherman","parturient montes,","nec@idmagnaet.co.uk"))
contest_list.append(Contests("placerat. Cras dictum","2020-08-06 07:25:03","2019-02-22 16:47:57","2019-10-11 14:39:02","2019-10-03 11:03:18","2019-07-17 03:39:56",10,16,8,"Hayes Everett","rhoncus.Nullam@erat.net","(645) 887-1512","nisi a","Quon Clayton","at auctor","In@magnaNam.com"))
contest_list.append(Contests("pellentesque a, facilisis","2020-04-24 06:53:08","2019-10-29 23:35:00","2018-11-29 21:25:03","2019-03-04 14:21:28","2020-06-23 12:54:47",13,16,7,"Janna Barry","Curabitur@Phasellus.ca","(209) 596-6338","eleifend non,","Clare Bender","ridiculus mus.","ac.nulla@magnis.com"))
contest_list.append(Contests("eget magna. Suspendisse","2020-06-24 08:28:58","2020-02-12 05:41:14","2020-07-10 07:30:10","2019-06-14 22:16:44","2020-01-28 07:55:33",11,14,5,"Oren Welch","lectus.convallis@sodaleselit.net","(432) 728-8488","malesuada fames","Elizabeth Hurst","elementum sem,","risus@pedeet.org"))
contest_list.append(Contests("fermentum convallis ligula.","2019-07-19 06:02:03","2018-11-22 22:56:04","2020-07-05 09:46:20","2019-07-10 14:13:18","2020-04-11 16:01:27",11,16,7,"Shay Michael","cursus.Nunc@velturpis.com","(536) 130-0586","enim commodo","Driscoll Pruitt","dis parturient","risus.Quisque.libero@egetvolutpatornare.ca"))
contest_list.append(Contests("et magnis dis","2020-01-23 12:40:36","2019-04-23 23:12:47","2019-01-23 05:16:45","2019-04-22 16:03:01","2019-07-27 03:49:02",11,15,7,"Emi Soto","ante@metusInnec.com","(940) 932-1207","Suspendisse non","Meghan Fox","erat. Vivamus","ac.urna@semper.edu"))
contest_list.append(Contests("lacinia vitae, sodales","2020-08-13 16:18:08","2018-12-02 02:54:39","2019-11-16 16:30:56","2020-04-10 08:51:22","2020-02-02 01:03:16",9,15,6,"Quamar Guerra","ipsum.nunc@velnisl.com","(118) 572-1689","purus sapien,","Hedley Powell","Integer aliquam","nec@Donec.ca"))
contest_list.append(Contests("cursus luctus, ipsum","2020-08-11 02:03:45","2018-12-15 01:55:01","2018-10-11 02:49:57","2020-04-05 04:57:56","2019-03-19 17:26:07",9,15,6,"Linus Miles","mollis@Curae.com","(665) 619-0577","eu, eleifend","Lillian Patterson","ut quam","non@placerat.edu"))
contest_list.append(Contests("nonummy ac, feugiat","2020-01-15 04:42:37","2019-09-27 11:36:41","2018-11-30 12:23:58","2020-07-26 11:23:59","2019-06-26 03:38:10",12,17,5,"Channing Mcgowan","eu.erat.semper@etrutrum.net","(663) 564-0797","Nunc ut","Perry Stanley","gravida non,","mauris.rhoncus@Namtempordiam.org"))

##loop though contest_list and add each contest object to be committed
for contest in contest_list:
    db.session.add(contest)

db.session.commit()

##add several Events objects to a list of Events##
events_list.append(Events("a sollicitudin orci",20,"Suspendisse eleifend.","Aliquam ultrices iaculis odio. Nam interdum enim non nisi. Aenean eget metus.",10))
events_list.append(Events("fringilla euismod enim.",22,"semper erat,","lectus pede et risus. Quisque libero lacus, varius et, euismod et, commodo at, libero.",9))
events_list.append(Events("dictum sapien. Aenean",20,"orci. Ut","pede. Praesent eu dui. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean eget magna. Suspendisse tristique neque venenatis lacus.",3))
events_list.append(Events("mauris blandit mattis.",21,"diam luctus","ut cursus luctus, ipsum leo elementum sem, vitae aliquam eros turpis non enim.",1))
events_list.append(Events("ut nisi a",23,"posuere cubilia","at fringilla purus mauris a nunc. In at pede. Cras vulputate velit eu sem. Pellentesque ut ipsum ac mi eleifend egestas. Sed pharetra, felis eget varius ultrices, mauris ipsum porta elit, a",6))
events_list.append(Events("Vivamus euismod urna.",20,"Nam tempor","tincidunt adipiscing. Mauris molestie pharetra nibh. Aliquam ornare, libero at auctor ullamcorper, nisl arcu iaculis enim, sit amet ornare lectus justo eu arcu. Morbi sit amet massa.",8))
events_list.append(Events("dolor. Quisque tincidunt",27,"senectus et","orci sem eget massa. Suspendisse eleifend. Cras sed leo. Cras vehicula aliquet libero. Integer in magna. Phasellus dolor elit, pellentesque a, facilisis non, bibendum sed,",2))
events_list.append(Events("nisl arcu iaculis",29,"mi, ac","commodo ipsum. Suspendisse non leo. Vivamus nibh dolor, nonummy ac, feugiat non, lobortis quis, pede. Suspendisse dui. Fusce diam nunc, ullamcorper eu, euismod ac, fermentum vel, mauris. Integer sem elit, pharetra ut, pharetra",4))
events_list.append(Events("convallis erat, eget",22,"Duis cursus,","tincidunt nibh. Phasellus nulla. Integer vulputate, risus a ultricies adipiscing, enim mi tempor lorem, eget mollis lectus pede et risus. Quisque libero lacus, varius et, euismod et, commodo at, libero. Morbi accumsan",5))
events_list.append(Events("vel, mauris. Integer",24,"ultrices, mauris","lobortis mauris. Suspendisse aliquet molestie tellus. Aenean egestas hendrerit neque. In ornare sagittis felis. Donec tempor, est ac mattis semper, dui lectus rutrum urna, nec",7))

##loop though events_list and add each event object to be committed
for event in events_list:
    db.session.add(event)

db.session.commit()

##add several Schools objects to a list of Schools##
schools_list.append(Schools("massa lobortis ultrices. Vivamus","Ap #231-1037 Adipiscing St.","Fontecchio","7739","1-877-387-8777","non.feugiat@dolorsitamet.com",generate_password_hash("cat"),"Lance Mullen","Nunc.commodo.auctor@idanteNunc.edu",10))
schools_list.append(Schools("diam lorem, auctor quis,","Ap #793-1621 Auctor Street","Cisterna di Latina","59955","1-328-437-3728","pede.malesuada.vel@tinciduntadipiscingMauris.org",generate_password_hash("dog"),"Dennis Ferrell","mauris.Integer.sem@tortordictumeu.com",5))
schools_list.append(Schools("dolor dolor, tempus non,","P.O. Box 966, 9973 Orci, Ave","Cordoba","30915","1-840-962-4523","Suspendisse.aliquet.molestie@eleifend.edu",generate_password_hash("rat"),"Jason Tanner","ac.turpis@Phaselluselit.edu",9))
schools_list.append(Schools("sollicitudin a, malesuada id,","P.O. Box 634, 2568 Libero. Rd.","Waret-l'Evque","40317","1-985-932-0808","elit@lorem.ca",generate_password_hash("monkey"),"Cally Kent","massa.lobortis@eros.ca",3))
schools_list.append(Schools("velit eget laoreet posuere,","Ap #826-2412 Fermentum Rd.","Kleinmachnow","20322","1-944-693-2779","placerat.velit@loremfringillaornare.edu",generate_password_hash("fish"),"Noelani Griffin","eu.placerat@vel.com",7))
schools_list.append(Schools("scelerisque scelerisque dui. Suspendisse","P.O. Box 301, 4797 Magna St.","Innisfail","55-909","1-802-889-5786","Vestibulum@Cum.co.uk",generate_password_hash("owl"),"Jacqueline Tyson","at.auctor@Sedeunibh.com",4))
schools_list.append(Schools("nascetur ridiculus mus. Proin","Ap #377-4384 Risus. St.","Salamanca","79399","1-159-916-7796","pede.malesuada.vel@euismodestarcu.ca",generate_password_hash("tiger"),"Andrew Johns","arcu.et@arcuSed.org",8))
schools_list.append(Schools("auctor non, feugiat nec,","Ap #108-2746 Lectus Road","Opoeteren","88637","1-781-883-1083","tellus.faucibus.leo@consectetuer.co.uk",generate_password_hash("turdle"),"Alexandra Gay","ut.erat.Sed@nullamagna.edu",6))
schools_list.append(Schools("purus mauris a nunc.","Ap #286-2515 Congue. Avenue","Narcao","73556","1-308-730-7294","Mauris.ut.quam@maurisutmi.co.uk",generate_password_hash("bat"),"Beverly Santos","sollicitudin.orci.sem@ut.ca",2))
schools_list.append(Schools("nec ligula consectetuer rhoncus.","764-297 Non, Rd.","Tarcento","3978","1-180-722-1998","tempor.erat@idblandit.edu",generate_password_hash("mouse"),"Felix Rios","bibendum.ullamcorper@dignissimMaecenasornare.org",1))

##loop though schools_list and add each school object to be committed
for school in schools_list:
    db.session.add(school)

db.session.commit()

##add several Teachers objects to a list of Teachers##
teachers_list.append(Teachers("Rafael Schmidt","Curabitur.sed.tortor@convallisest.co.uk",1))
teachers_list.append(Teachers("Madonna Hendricks","sit@Fuscefeugiat.net",3))
teachers_list.append(Teachers("September Morales","orci@nullamagnamalesuada.ca",4))
teachers_list.append(Teachers("Tatum Ramsey","ligula.Aenean.euismod@Nullamlobortis.org",5))
teachers_list.append(Teachers("Uma Francis","neque@Inornare.ca",6))
teachers_list.append(Teachers("Nero Bailey","lacinia.mattis@pede.org",2))
teachers_list.append(Teachers("Tatum Ballard","tempus@ornare.edu",7))
teachers_list.append(Teachers("Adria Love","enim.sit.amet@ascelerisque.com",10))
teachers_list.append(Teachers("Demetrius Farley","Donec@suscipitest.net",9))
teachers_list.append(Teachers("Sonia Mercer","feugiat@eratnonummy.net",8))

##loop though teachers_list and add each teacher object to be committed
for teacher in teachers_list:
    db.session.add(teacher)

db.session.commit()

##add several Students objects to a list of Students##
students_list.append(Students("Roanna","Davis",8,1))
students_list.append(Students("Colorado","Fuentes",5,2))
students_list.append(Students("Madeline","Justice",7,3))
students_list.append(Students("Joelle","Sanford",9,10))
students_list.append(Students("Declan","Mckee",4,4))
students_list.append(Students("Kevyn","Chandler",6,5))
students_list.append(Students("Charde","Brewer",10,6))
students_list.append(Students("Giselle","Dillon",1,7))
students_list.append(Students("Charde","Chavez",2,9))
students_list.append(Students("Mufutau","Coleman",3,8))

##loop though students_list and add each student object to be committed
for student in students_list:
    db.session.add(student)

db.session.commit()

##add several Pictures objects to a list of Pictures##
pictures_list.append(Pictures("et magnis dis parturient montes, nascetur","indigo.jpg",5))
pictures_list.append(Pictures("ut, pharetra sed, hendrerit a, arcu. Sed et","violet.jpg",3))
pictures_list.append(Pictures("Phasellus at augue","blue.jpg",1))
pictures_list.append(Pictures("Sed auctor odio a purus. Duis elementum, dui quis","green.jpg",4))
pictures_list.append(Pictures("vel, vulputate eu, odio. Phasellus at augue","orange.jpg",2))
pictures_list.append(Pictures("lacinia. Sed congue, elit sed","violet.jpg",6))
pictures_list.append(Pictures("congue a, aliquet vel, vulputate eu,","red.jpg",8))
pictures_list.append(Pictures("facilisis vitae, orci. Phasellus","green.jpg",9))
pictures_list.append(Pictures("placerat","orange.jpg",10))
pictures_list.append(Pictures("ligula consectetuer rhoncus. Nullam velit dui, semper et,","blue.jpg",7))

##loop though pictures_list and add each picture object to be committed
for picture in pictures_list:
    db.session.add(picture)

db.session.commit()

##Creating an Admin##
admin_username = "admin"
admin_password = generate_password_hash("bcc2016")

db.session.add(Admins(admin_username, admin_password))

db.session.commit()