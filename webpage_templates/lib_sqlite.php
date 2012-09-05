<?php
    // func =================================
    function get_db_data($db_name){
        
        $link = db_open($db_name);
        
        $sql = "SELECT * FROM $db_name";
        $query = sqlite_query($link, $sql);
        $result = sqlite_fetch_all($query, SQLITE_ASSOC);
        
//        echo "[".basename(__FILE__).":".__LINE__."]"."<br/>\n";
//        $query = sqlite_query(db_open)
        
        db_close($link);
        
        return $result;
//        echo "[".basename(__FILE__).":".__LINE__."]"."<br/>\n";
    
    }//function open_db($db_name){    
?>
<! -- created_at: 20111123_060948_php_handle_labdata_1 -->
<! -- version: 1.0 -->
<! -- debug: echo "[".basename(__FILE__).":".__LINE__."]" -->
