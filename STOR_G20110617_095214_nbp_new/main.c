#include <stdio.h>
#include <stdlib.h>

//v=1.0

int main( void )
{
    char ss[] = "abc";
    char * p = ss;

    printf("Content-Type: text/html;charset=shift-jis\n\n");
    printf(__FILE__); printf("<br>\n");
    
    printf("p(%%p)=%p\n", p); printf("<br>\n");
    printf("p(%%s)=%s\n", p); printf("<br>\n");
    printf("putchar(*p)=");
    putchar(*p); printf("<br>\n");
    putchar('\n');
    printf("putchar(*(p+1))=");
    putchar(*(p+1)); printf("<br>\n");
    putchar('\n');

/*
    printf("putchar(p)=");
    putchar(p);
    putchar('\n'); printf("<br>\n");
*/

    //04
    printf("printf(\"%%d\")=%d\n", p); printf("<br>\n");
    printf("printf(\"%%x\")=%x\n", p); printf("<br>\n");

    //06
    printf("<06>\n");
    
    char * cp;
    int * ip;

    printf("ss(%%s)=%s ss(%%p)=%p\n", ss, ss);
    cp = ss;
    printf("cp(%%p)=%p *cp(%%c)=%c\n", cp, *cp);
    printf("cp(%%s)=%s\n", cp);
    printf("cp+1(%%s)=%s\n", (cp+1));
    printf("cp+2(%%s)=%s\n", (cp+2));
    printf("cp+3(%%s)=%s\n", (cp+3));
    printf("cp+4(%%s)=%s\n", (cp+4));
/*
    printf("*cp(%%s)=%s\n", *cp);
*/
    
/*
    int * a;
    a = 120;
*/
/*
    i = 20;
*/
    return 0;
}

