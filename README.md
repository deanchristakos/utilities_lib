The config_mapper file has the ConfigSectionMap class that takes the name of a  config file in the constructor that creates a dictionary out of the config values. 
The config files are divided into "Sections" specfied by [Square Brackets] follow by key-value pairs separated by colons, eg:

[Database]

DbHost: dbhostname

DBName: databasename

User: username

Password: password1

You'd do the following:

mapper = ConfigSectionMap(configfile)

db_name = mapper.sectionMap('Database')['dbname']
