''' 
@begin MenuItemDataCleanupWorkflow @desc This workflow is for MenuItem.csv dataset cleanup 
@in MenuItem.csv @uri file://project/MenuItem.csv
    
    @begin MenuItemDataCleanupWithOpenRefine @desc Clean MenuItem dataset using OpenRefine
    @in MenuItem.csv @uri file://project/MenuItem.csv
    @out cleaned_menu_item_with_or.csv @uri file://project/clean/cleaned_menu_item_with_or.csv
    @end MenuItemDataCleanupWithOpenRefine
    
    @begin LoadMenuItemDataIntoSqlite @desc Load cleaned_dish_with_or.csv into Sqlite table menu_item
    @in cleaned_menu_item_with_or.csv @uri file://project/cleaned_menu_item_with_or.csv
    @param data_load_script
    @out menu_item @uri sqlite://database.db/menu_item
    @end LoadMenuItemDataIntoSqlite
    
    @begin MenuItemDataCleanupWithSQL @desc Perform SQL operations to check integrity constraints and functional dependencies
    @in menu_item @uri sqlite://database.db/menu_item
    @param data_cleanup_sql_script
    @out cleaned_menu_item @uri sqlite://database.db/cleaned_menu_item
    @end MenuItemDataCleanupWithSQL
    

@out cleaned_menu_item @uri sqlite://database.db/cleaned_menu_item
@end DataCleanup

'''