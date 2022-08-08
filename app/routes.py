from mvc_flask import Router


Router.get("/",             "home#index")
Router.all("posts",         only="show new create")
Router.all("categories",    only="new create")
Router.all("signup",        only="new create")
Router.all("signin",        only="new create")