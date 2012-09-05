<?php
    require("lib.php");

    $FILE_INFO = <<<INFO
        Vars:
            
        Flow:
        
INFO;

    require(@TEMPLATE_FILE@);
?>

<! -- file name: @FILE_NAME@ -->
<! -- created_at: @CREATED_AT@ -->
<! -- version: @VERSION@ -->
<! -- debug: echo "[".basename(__FILE__).":".__LINE__."]" -->
<! -- debug: echo "<br/>"."\n"; -->
