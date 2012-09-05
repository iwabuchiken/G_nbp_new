<html>
    <head>
            <title><?php echo basename(__FILE__); ?></title>
            <link rel="stylesheet" type="text/css" 
                  href="<?= join("/",
                            array ($url_root, "tools", "css", "main.css")) ?>" />
    </head>
    <body>
        <div>
            <?= basename(__FILE__); ?>
        </div>
    </body>
</html>

<! -- file name: @FILE_NAME@ -->
<! -- created_at: @CREATED_AT@ -->
<! -- version: @VERSION@ -->
<! -- debug: echo "[".basename(__FILE__).":".__LINE__."]" -->
