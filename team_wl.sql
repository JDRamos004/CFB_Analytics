DROP DATABASE IF EXISTS cfb_data;
CREATE DATABASE IF NOT EXISTS cfb_data;

USE cfb_data;

DROP TABLE IF EXISTS team_wl;
CREATE TABLE team_wl
(
	team_name VARCHAR(40) NOT NULL,
    conf_win INT NOT NULL,
    conf_loss INT NOT NULL,
    wins INT NOT NULL,
    losses INT NOT NULL,
    points_for INT NOT NULL,
    points_against INT NOT NULL,
    streak VARCHAR(12) NOT NULL
    );
    
SELECT * FROM team_wl;