CREATE TABLE `users` (
  `id` int PRIMARY KEY,
  `firstname` varchar(255),
  `lastname` varchar(255),
  `email` varchar(255),
  `adresse` varchar(255),
  `Phonenumber` int,
  `created_at`varchar(255),
  `updated_add` varchar(255)
);

CREATE TABLE `courses` (
  `id_courses` int PRIMARY KEY,
  `name_courses` varchar(255),
  `description` varchar(255),
  `date_courses` date,
  `duree_courses` int,
  `id_enseignant` int,
  `id_salle` int,
  `created_at`varchar(255),
  `updated_at` varchar(255)
);

CREATE TABLE `enseignants` (
  `id_enseignants` int PRIMARY KEY,
  `firstname_enseignant` varchar(255),
  `prenom_enseignant` varchar(255),
  `email` varchar(255),
  `adresse` varchar(255),
  `Phone` int,
  `created_at` varchar(255),
  `updated_at`varchar(255)
);

CREATE TABLE `salles` (
  `id_salles` int PRIMARY KEY,
  `id_courses` int,
  `dimensions` int,
  `created_at` varchar(255),
  `updated_at` varchar(255)
);

CREATE TABLE `inscriptions` (
  `id_inscription` int PRIMARY KEY,
  `id_etudiant` int,
  `date_inscription` date,
  `created_at` varchar(255),
  `updated_at` varchar(255)
);

CREATE TABLE `students` (
  `id_students` int PRIMARY KEY,
  `firstname_student` varchar(255),
  `lastname_student` varchar(255),
  `id_courses` int,
  `date_inscription` date,
  `id_inscription` int,
  `created_at` varchar(255),
  `updated_at` varchar(255)
);

CREATE TABLE `emloidutemps` (
  `id_emploi` int PRIMARY KEY,
  `jour` int,
  `created_at` varchar(255),
  `updated_add` varchar(255)
);

CREATE TABLE `shedule` (
  `id_shedule` int PRIMARY KEY,
  `hour` int,
  `id_salles` int,
  `created_at` varchar(255),
  `updated_at` varchar(255)
);

CREATE TABLE `modules` (
  `id_modules` int PRIMARY KEY,
  `name_modules` varchar(255),
  `id_shedule` int,
  `created_at` varchar(255),
  `updated_at` varchar(255)
);

ALTER TABLE `courses` ADD FOREIGN KEY (`name_courses`) REFERENCES `courses` (`id_courses`);

ALTER TABLE `courses` ADD FOREIGN KEY (`id_courses`) REFERENCES `users` (`id`);

ALTER TABLE `courses` ADD FOREIGN KEY (`id_courses`) REFERENCES `enseignants` (`id_enseignants`);

ALTER TABLE `courses` ADD FOREIGN KEY (`id_courses`) REFERENCES `inscriptions` (`id_inscription`);

ALTER TABLE `inscriptions` ADD FOREIGN KEY (`id_inscription`) REFERENCES `students` (`id_students`);

ALTER TABLE `salles` ADD FOREIGN KEY (`id_salles`) REFERENCES `courses` (`id_courses`);

ALTER TABLE `modules` ADD FOREIGN KEY (`id_modules`) REFERENCES `shedule` (`id_shedule`);

ALTER TABLE `emloidutemps` ADD FOREIGN KEY (`id_emploi`) REFERENCES `courses` (`id_courses`);

ALTER TABLE `shedule` ADD FOREIGN KEY (`id_shedule`) REFERENCES `courses` (`id_courses`);

ALTER TABLE `shedule` ADD FOREIGN KEY (`id_shedule`) REFERENCES `salles` (`id_salles`);
