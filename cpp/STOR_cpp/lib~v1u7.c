#include <stdio.h>
#include <stdlib.h>

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

// func defs -------------------------
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
