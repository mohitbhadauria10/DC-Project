''' 
@begin MenuPageDataCleanupWorkflow @desc This workflow is for MenuPage.csv dataset cleanup
@in MenuPage.csv @uri file://project/MenuPage.cv
    
    @begin MenuPageDataCleanupWithOpenrRefine @desc Clean MenuPage dataset using OpenRefine
    @in MenuPage.csv @uri file://project/MenuPage.cv
    @out cleaned_menu_page_with_or.csv @uri file://project/cleaned_menu_page_with_or.csv
    @end MenuPageDataCleanupWithOpenrRefine
    
    @begin LoadMenuPageDataIntoSqlite @desc Load cleaned_menu_page_with_or.csv into Sqlite table menu_page
    @in cleaned_menu_page_with_or.csv @uri file://project/cleaned_menu_page_with_or.csv
    @param data_load_script
    @out menu_page @uri sqlite://database.db/menu_page
    @end LoadMenuPageDataIntoSQLLIte
    
    
    @begin MenuPageDataCleanupWithSQL @desc Perform SQL operations to check integrity constraints and functional dependencies
    @in menu_page @uri sqlite://database.db/menu_page
    @param data_cleanup_sql_script
    @out cleaned_menu_page @uri sqlite://database.db/cleaned_menu_page
    @end MenuPageDataCleanupWithSQL
    
@out MENU_PAGE_FINAL @uri sqlite://database.db/cleaned_menu_page
@end DataCleanup

'''