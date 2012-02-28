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

#ifndef FILE_INFO
#define FILE_INFO
#define CREATED_AT "undefined"
#define MODIFIED_AT "undefined"
#define FILE_VERSION "undefined"
#endif

#ifndef INCLUDE_STRING_H
#define INCLUDE_STRING_H
#include <string.h>
#endif

#include <time.h>
//#include "main_c.h"

//file_info: v=1.6

// prototypes -------------------------
int confirm( void );
char * get_fname( char *fname_in, char *ext );
char * get_fname2( char *fname_in, char *ext, char **memo );
char * get_time_label( void );
void show_fileinfo( void );
int xtod( int x );
int little_endian_convert( int xnum[], int n );
int func2(char *dst, char *src);
FILE *open_file( char *fname, const char *mode );
int get_max( int *num, int size, int *index ); // 2011/11/06-19:57:44

// func defs -------------------------
#ifdef D
int main( int argc, char *argv[] )
{
    printf("[%s:%d]\n", __FILE__, __LINE__);
    
}//int main( int argc, char *argv[] )
#endif

FILE *open_file( char *fname, const char *mode )
{
    FILE *fp;

    // 01 open file
    fp = fopen(fname, "rb");
    if (fp == NULL) {
        printf("Can't open the file: %s\n", fname);
        return NULL;
    } else {
        printf("File opened: %s\n", fname);
        return fp;
    }//if (fp == NULL) {
}//FILE *open_file( char *fname )

int func2(char *dst, char *src)
{
    //int i = 0; // counter
    int i = -1; // counter
    int ret = -1;

    //while (src[i++]) {
    while (src[++i]) {
        printf("[LINE:%d]", __LINE__);
        printf("i=%d src[%d]=%c\n", i, i, src[i]);
        
        if (src[i] == '.') ret = i;
    }
    // readjust
    if (ret == 0) ret = -1;

    // 02 input base name
    if (ret != -1) {
        for (i = 0; i < ret; i++)
            dst[i] = src[i];
    }
    dst[i] = '\0';
    
    return ret;
}//int func2(char *dst, char *src)

int little_endian_convert( int xnum[], int n )
{
    int i; // counter
    int *d;
    int d_sum = 0;

    d = calloc(n, sizeof(int));
    
    for (i = 0; i < n; i++)
        d[i] = xtod(xnum[i]);

    for (i = (n - 1); i >= 0; i --)
        d_sum += d[i] * pow(256, (i));
    
    free(d);

    return d_sum;
}//int little_endian_convert()

int xtod( int x )
/*
 * Usage: Example
 *  => int d = xtod(0xA0);
 */
{
    int d;
    char *tmp;

    tmp = malloc(sizeof(char) * 4);

    sprintf(tmp, "%d", x);

    d = atoi(tmp);

    return d;
}

int confirm( void ) {
    int ans;

    while (1) {
        printf("Continue? y=1/n=0: ");
        scanf("%d", &ans);
        if (ans == 1) return 1;
        else if (ans == 0) return 0;
        else printf("Neither 1 nor 0. Loop continues.\n");
    }//while (1) {
}//void confirm( void ) {

char * get_fname( char *fname_in, char *ext ) {

    char *time_label = NULL;
    char *fname_out = calloc(strlen(fname_in)+20,
                            sizeof(char));
    time_label = get_time_label();
    sprintf(fname_out, "%s_%s.%s",
                    fname_in, time_label, ext);
//    sprintf(fname_out, "%s_%s.pgm", fname_in, time_label);


    free(time_label);



    return fname_out;

}//char * get_fname( char *fname_in ) {

char * get_time_label( void )
{


    time_t current;
    struct tm *local;
    char * label = NULL;

    label = malloc(sizeof(char) * 20);

    time(&current);
    local = localtime(&current);
    strftime(label, 255, "%Y%m%d_%H%M%S", local);

    return label;

}//char * get_time_label( void )

void show_fileinfo( void )
{
    printf("created at=%s\n", CREATED_AT);
    printf("modified at=%s\n", MODIFIED_AT);
    printf("file version=%s\n", FILE_VERSION);
}

char * get_fname2( char *fname_in, char *ext, char **memo )
{
#ifdef D
printf("[%s:%d] ", __FILE__, __LINE__);
printf("memo[0]=%s\n", memo[0]);
printf("strlen(memo[0])=%d\n", strlen(memo[0]));
#endif

    char *time_label = NULL;
    char *fname_out = calloc(
                strlen(fname_in)
                +strlen(memo[0])
                +strlen(ext)+20, sizeof(char));
    time_label = get_time_label();
    sprintf(fname_out, "%s_%s_%s.%s",
                fname_in, time_label, memo[0], ext);
    free(time_label);
#ifdef D
printf("[%s:%d] ", __FILE__, __LINE__);
printf("memo[0]=%s\n", memo[0]);
printf("fname_out=%s\n", fname_out);
exit(0);
#endif
    return fname_out;
    //strcpy(memo[0], "and the story goes on...");
/*
    sprintf(memo[0], "and the story '%s' goes on...",
                    "NEW");

    return NULL;
*/
/*
    char *time_label = NULL;
    char *fname_out = calloc(strlen(fname_in)+20,
                            sizeof(char));
    time_label = get_time_label();
    sprintf(fname_out, "%s_%s.%s",
                    fname_in, time_label, ext);
//    sprintf(fname_out, "%s_%s.pgm", fname_in, time_label);


    free(time_label);



    return fname_out;
*/

}//char * get_fname2( char *fname_in, char *ext, char **memo )

int get_max( int *num, int size, int *index )
{
    int max = 0;
    int i; // counter
    *index = -1;

/*
    printf("sizeof(num)/sizeof(num[0])=%d\n",
                sizeof(num)/sizeof(num[0]));
*/
    for (i = 0; i < size; i++) {
        if (max < num[i]) {
            max = num[i]; *index = i;
        }
    }

    //printf("max=%d(index=%d)\n", max, *index);

    return max;
}//int get_max( int *num, int size, int *index )

/*
#ifdef D
    printf("[%s:%d]", __FILE__, __LINE__);
#endif
*/
