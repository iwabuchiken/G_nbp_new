<?php
    // vars
    $url_root = dirname(dirname($_SERVER['PHP_SELF']));
    $dir_root = dirname(dirname(__FILE__));

@VAR_LIST_CONTROL@
@VAR_LIST_VIEW@
    // func =================================
    function db_open($db_name){
        
        $link = sqlite_open($db_name, 0666, $sqliteerror);
    
        if (!$link) {
        die('Ú‘±Ž¸”s‚Å‚·B'.$sqliteerror);
        }
        
        return $link;
    }//function open_db($db_name){
    
    function db_close($link){
        sqlite_close($link);
    }
    
    function show_msg(){
        echo "[".basename(__FILE__).":".__LINE__."]"."<br/>\n";
    }//function show_msg(){
?>
<! -- created_at: 20111123_060948_php_handle_labdata_1 -->
<! -- version: 1.0 -->
<! -- debug: echo "[".basename(__FILE__).":".__LINE__."]" -->
