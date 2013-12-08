---
layout: post
title: Migrations in Rails 4
category: Ruby
tags: [Ruby, Rails, Rake, Database]
---

Rails encourages an agile, iterative style of development. We don’t expect to get everything right the first time. Instead, we write tests and interact with our customers to refine our understanding as we go.

For that to work, we need a supporting set of practices. We write tests to help us design our interfaces and to act as a safety net when we change things, and we use version control to store our application’s source files, allowing us to undo mistakes and to monitor what changes day to day.

But there’s another area of the application that changes, an area that we can’t directly manage using version control. The database schema in a Rails application constantly evolves as we progress through the development: we add a table here, rename a column there, and so on. The database changes in step with the application’s code.

##Migrations

A migration is simply a Ruby source file in your application’s `db/migrate` directory. Each migration file’s name starts with a number of digits (typically fourteen) and an underscore. Those digits are the key to migrations, because they define the sequence in which the migrations are applied - they are the individual migration’s version number.

The migration code maintains a table called `schema_migrations` inside every Rails database. This table has just one column, called `version`, and it will have one row per successfully applied migration.

under migrate directory

    $ ls depot/db/migrate

    20131104093431_create_products.rb
    20131105023033_create_carts.rb
    20131105023651_create_line_items.rb
    20131105033211_add_quantity_to_line_items.rb
    20131105034630_combine_items_in_cart.rb
    20131105083930_create_orders.rb
    20131105083959_add_order_to_line_item.rb
    20131106005643_create_users.rb
    
migrations are run using the `db:migrate` Rake task, like:

    % rake db:migrate
    
sqlite3 

    $ rails db
    SQLite version 3.7.15.2 2013-01-09 11:53:05
    Enter ".help" for instructions
    Enter SQL statements terminated with a ";"
    sqlite> .headers on
    sqlite> select * from schema_migrations;
    version
    20131104093431
    20131105023033
    20131105023651
    20131105033211
    20131105034630
    20131105083930
    20131105083959
    20131106005643

Using migrations, you can:

* create, rename, and delete columns and tables.
* manage indices and keys.
* apply and back out entire sets of changes.
* mix in your own custom SQL into the mix, all in a completely reproducible manner.

###Column Types

Rails tries to make your application independent of the underlying database; you could develop using SQLite 3 and deploy to Postgres if you wanted, for example.

Rails migrations insulate you from the underlying database type systems by using logical types, like:

![rails4_migration_types](http://dylanninin.com/assets/images/2013/rails/rails4_migration_types.png)

There are three options you can use when defining most columns in a migration. Each of these options is given as a `key: value` pair. The common options are as follows:

* null: true or false. If false, the underlying column has a not null constraint added (if the database supports it).
* limit: size. This sets a limit on the size of the field.
* default: value. This sets the default value for the column.
* `decimal` columns take the options `:precision` and `:scale`. The `:precision` option specifies the number of significant digits that will be stored, and the `:scale` option determines where the decimal point will be located in these digits.

###Migrations with Rake

    $ rake -T | grep db
    rake db:create                          # Create the database from DATABASE_URL or config/database.yml for the current Rails.env (use db:create:all to create all dbs in the config)
    rake db:drop                            # Drops the database using DATABASE_URL or the current Rails.env (use db:drop:all to drop all databases)
    rake db:fixtures:load                   # Load fixtures into the current environment's database
    rake db:migrate                         # Migrate the database (options: VERSION=x, VERBOSE=false, SCOPE=blog)
    rake db:migrate:status                  # Display status of migrations
    rake db:rollback                        # Rolls the schema back to the previous version (specify steps w/ STEP=n)
    rake db:schema:cache:clear              # Clear a db/schema_cache.dump file
    rake db:schema:cache:dump               # Create a db/schema_cache.dump file
    rake db:schema:dump                     # Create a db/schema.rb file that can be portably used against any DB supported by AR
    rake db:schema:load                     # Load a schema.rb file into the database
    rake db:seed                            # Load the seed data from db/seeds.rb
    rake db:setup                           # Create the database, load the schema, and initialize with the seed data (use db:reset to also drop the db first)
    rake db:structure:dump                  # Dump the database structure to db/structure.sql
    rake db:version                         # Retrieves the current schema version number
    rake test:all                           # Run tests quickly by merging all types and not resetting db
    rake test:all:db                        # Run tests quickly, but also reset db

##Reference

* [Agile Web Development with Rails 4](http://book.douban.com/subject/24718727/)
* [Rake (software)](http://en.wikipedia.org/wiki/Rake_(software))
* [Rake documentation](http://rake.rubyforge.org/)