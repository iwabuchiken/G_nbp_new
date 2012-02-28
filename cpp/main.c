/************************************`
 * <Basics>
 *	1. File: main.c					*
 *	2. Author: Iwabuchi Ken				*
 *	3. Date: 			*
 * <Aim>
 *	1.
 * <Usage>
 *	1.
 * <Source>
 *	1.
 ************************************/

#ifndef INCLUDE_STDIO
#define INCLUDE_STDIO
#include <stdio.h>
#endif
#ifndef INCLUDE_STDLIB
#define INCLUDE_STDLIB
#include <stdlib.h>
#endif
#ifndef INCLUDE_STRING
#define INCLUDE_STRING
#include <string.h>
#endif
#ifndef INCLUDE_TIME
#define INCLUDE_TIME
#include <time.h>
#endif
#ifndef INCLUDE_MATH
#define INCLUDE_MATH
#include <math.h>
#endif

//file_info

// structure, etc. ======================
typedef struct abc {
    int i;
} ABC;

// prototypes ======================
void func1( void );

// functions ======================
void func1( void )
{

}//void func1( void )

int main( int argc, char *argv[] )
{
    func1();

    return 0;
}//int main( int argc, char *argv[] )

/*
#ifdef D
    printf("[%s:%d]", __FILE__, __LINE__);
#endif

    printf("Content-Type: text/html;charset=shift-jis\n\n");
    printf(__FILE__); printf("<br>\n");
    printf(CREATED_AT); printf("<br>\n");
*/
