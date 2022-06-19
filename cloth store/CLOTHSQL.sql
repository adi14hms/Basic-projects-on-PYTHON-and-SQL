CREATE DATABASE `alumini_db` 

CREATE TABLE `log_in` (
  `customer_name` varchar(45) NOT NULL,
  `user id` int NOT NULL,
  `passkey` int NOT NULL,
  PRIMARY KEY (`customer_name`,`user id`,`passkey`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `sales_cloth` (
  `employ_name` varchar(45) NOT NULL,
  `item_sale` varchar(45) NOT NULL,
  `bill` int NOT NULL,
  `customer name` varchar(45) NOT NULL,
  `customer_phone` int NOT NULL,
  PRIMARY KEY (`employ_name`,`item_sale`,`bill`,`customer name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci