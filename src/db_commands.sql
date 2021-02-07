DROP DATABASE IF EXISTS `quiz_db`;  

CREATE DATABASE `quiz_db`;

USE `quiz_db`;

/*Table structure for table `easy_quiz_table` */

DROP TABLE IF EXISTS `easy_quiz_table`;

CREATE TABLE `easy_quiz_table`(
  `question_id` VARCHAR(20) PRIMARY KEY,
  `questions` VARCHAR(200) NOT NULL,
  `option1` VARCHAR(100) NOT NULL,
  `option2` VARCHAR(100) NOT NULL,
  `option3` VARCHAR(100) NOT NULL,
  `option4` VARCHAR(100) NOT NULL,
  `answer` VARCHAR(20) NOT NULL
  
);

/*Table structure for table `medium_quiz_table` */
DROP TABLE IF EXISTS `medium_quiz_table`;

CREATE TABLE `medium_quiz_table`(
  `question_id` VARCHAR(20) PRIMARY KEY,
  `questions` VARCHAR(200) NOT NULL,
  `option1` VARCHAR(100) NOT NULL,
  `option2` VARCHAR(100) NOT NULL,
  `option3` VARCHAR(100) NOT NULL,
  `option4` VARCHAR(100) NOT NULL,
  `answer` VARCHAR(20) NOT NULL
  
);

/*Table structure for table `hard_quiz_table` */
DROP TABLE IF EXISTS `hard_quiz_table`;

CREATE TABLE `hard_quiz_table`(
  `question_id` VARCHAR(20) PRIMARY KEY,
  `questions` VARCHAR(200) NOT NULL,
  `option1` VARCHAR(100) NOT NULL,
  `option2` VARCHAR(100) NOT NULL,
  `option3` VARCHAR(100) NOT NULL,
  `option4` VARCHAR(100) NOT NULL,
  `answer` VARCHAR(20) NOT NULL
  
);

/*Table structure for table `results` */
DROP TABLE IF EXISTS `results`;
CREATE TABLE `results`(
    `user_id` VARCHAR(20) PRIMARY KEY,
    `user_name` VARCHAR(50) NOT NULL,
    `total_score` VARCHAR(50) NOT NULL
);









