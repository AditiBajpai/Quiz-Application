USE `quiz_db`;

INSERT INTO easy_quiz_table(`question_id`,`questions`,`option1`,`option2`,`option3`,`option4`,`answer`) values
("E0_1","Which animal is known as 'Ship of the Desert'?","Horse","Camel","Giraffe","Elephant","Camel"),
("E0_2", "Which month of the year has the least number of days?", "June","August","February","May","February"),
("E0_3", "How may sides are there in a triangle?", "Seven","four","Six","Three","Three"),
("E0_4", "How many consonants are there in english alphabet?", "21","4","5","22","21"),
("E0_5", "Which is the principal source of energy for earth?", "Moon","Jupiter","Sun","River","Sun");

INSERT INTO medium_quiz_table(`question_id`,`questions`,`option1`,`option2`,`option3`,`option4`,`answer`) values
("M0_1","What is the largest moon of Saturn called?","Titan","Pan","Daphnis","None of the Above","Titan"),
("M0_2", "The Central Rice Research Station is situated in?", "Chennai","Cuttak","Bangalore","Quilon","Cuttak"),
("M0_3", "The metal whose salts are sensitive to light is?","Zinc","Silver","Copper","Aluminum","Silver"),
("M0_4", "Which country has the highest Barley production?", "China","India","Russia","France","Russia"),
("M0_5", "Tsunamis are not caused by which of the following?", "Hurricanes","Earthquakes","Undersea landslides","Volcanic Eruptions", "Hurricanes");

INSERT INTO hard_quiz_table(`question_id`,`questions`,`option1`,`option2`,`option3`,`option4`,`answer`) values
("H0_1","The hottest planet in the solar system?","Jupiter","Mars","Mercury","Venus","Venus"),
("H0_2", "Where was electricity supply first intriduced in India?", "Darjeeling","Dehradun","Mumbai","Pune","Darjeeling"),
("H0_3","Which peninsular river is least seasonal in flow?", "Narmada","Krishna","Godavari","Cauvery","Godavari"),
("H0_4","Guwahati High Court is the judicature of?", "Assam","Nagaland","Arunachal Pradesh","All of the Above","All of the Above"),
("H0_5", "First China War was fought between?","China and Egypt","China and Greek","China and Britain","China and France","China and Britain");
