''' 
@begin DishDataCleanupWorkflow @desc his workflow is for Dish.csv dataset cleanup
@in Dish.csv @uri file://project/Dish.csv

    @begin DishDataCleanupWithOpenRefine @desc Clean Dish dataset using OpenRefine
    @in Dish.csv @uri file://project/Dish.csv
    @out cleaned_dish_with_or.csv @uri file://project/cleaned_dish_with_or.csv
    @end DishDataCleanupWithOpenRefine
    
    @begin LoadDishDataIntoSqlite @desc Load cleaned_dish_with_or.csv into Sqlite table dish
    @in cleaned_dish_with_or.csv @uri file://project/cleaned_dish_with_or.csv
    @param data_load_script
    @out dish @uri sqlite://database.db/dish
    @end LoadDishDataIntoSqlite
    
    @begin DishDataCleanupWithSQL @desc Perform SQL operations to check integrity constraints and functional dependencies
    @in dish @uri sqlite://database.db/dish
    @param data_cleanup_sql_script
    @out cleaned_dish @uri sqlite://database.db/cleaned_dish
    @end DishDataCleanupWithSQL
    

@out cleaned_dish @uri sqlite://database.db/cleaned_dish
@end DataCleanup

'''