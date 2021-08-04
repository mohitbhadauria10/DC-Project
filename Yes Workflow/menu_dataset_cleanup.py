''' 
@begin MenuDataCleanupWorkflow @desc This workflow is for Menus.csv dataset cleanup
@in Menu.csv @uri file://project/Menu.csv

    @begin MenuDataCleanupWithOpenRefine @desc Clean Menu dataset using OpenRefine
    @in Menu.csv @uri file://project/Menu.csv
    @out cleaned_menu_with_or.csv @uri file://project/clean/cleaned_menu_with_or.csv
    @end MenuDataCleanupWithOpenRefine
    
    @begin LoadMenuDataIntoSqlite @desc Use SQLLite to load cleaned_menu_with_or.csv into table menu
    @in cleaned_menu_with_or.csv @uri file://project/clean/cleaned_menu_with_or.csv
    @param data_load_script
    @out menu @uri sqlite://database.db/menu
    @end LoadMenuDataIntoSqlite
    
    @begin MenuDataCleanupWithSQL @desc Perform SQL operations to check integrity constraints and functional dependencies
    @in menu @uri sqlite://database.db/menu
    @param data_cleanup_sql_script
    @out cleaned_menu @uri sqlite://database.db/cleaned_menu
    @end MenuDataCleanupWithSQL
    
@out cleaned_menu @uri sqlite://database.db/cleaned_menu
    
@end DataCleanup

'''