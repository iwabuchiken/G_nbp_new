#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "main_c.h"

//file_info

void confirm( void ) {
    int ans;

    while (1) {
        printf("Continue? y=1/n=0: ");
        scanf("%d", &ans);
        if (ans == 1) continue;
        else if (ans == 0) break;
        else printf("Neither 1 nor 0. Loop continues.\n");
    }//while (1) {
}//void confirm( void ) {

char * get_time_label()
{
    // Necessary to free 'time_label' 
    //in the function which called this function
    
    time_t current;
    struct tm *local;
    char * time_label;

    time_label = malloc(sizeof(20));

    time(&current);
    local = localtime(&current);
    strftime(time_label, 255, "%Y%m%d_%H%M%S", local);

    return time_label;
}//char * get_time_label()

void show_fileinfo()
{
    printf("created at=%s\n", CREATED_AT);
    printf("modified at=%s\n", MODIFIED_AT);
    printf("file version=%s\n", FILE_VERSION);
}

char *get_fname(char *fname) {
    char *ret = malloc(sizeof(strlen(fname) + 30));
    char *temp = malloc(sizeof(strlen(fname) + 30));
#ifdef D
    printf("[LINE:%d]", __LINE__);
    printf("temp: %%p=%p\n", temp);
    //exit(0);
#endif

    strcpy(temp, fname);
#ifdef D
    printf("[LINE:%d]", __LINE__);
    printf("'fname' copied to 'temp': %%p=%p\n", temp);
    //exit(0);
#endif

    char *time_label = get_time_label();

    if (ret == NULL) return NULL;
    if (temp == NULL) return NULL;
#ifdef D
    printf("[LINE:%d]", __LINE__);
    printf("temp=%s\n", temp);
    //exit(0);
#endif

    //char *token1 = strtok(fname, ".");
    char *token1 = strtok(temp, ".");
    char *token2 = strtok(NULL, ".");
#ifdef D
    printf("[LINE:%d]", __LINE__);
    printf("token1=%s token2=%s\n", token1, token2);
#endif

#ifdef D
    printf("[LINE:%d]", __LINE__);
    printf("time_label=%s\n", time_label);
#endif
    sprintf(ret, "%s_%s.%s", token1, time_label, token2);
#ifdef D
    printf("[LINE:%d]", __LINE__);
    printf("time_label=%s %%p=%p\n", time_label, time_label);
    printf("ret=%s %%p=%p\n", ret);
#endif

    //free(time_label);
#ifdef D
    printf("[LINE:%d]", __LINE__);
    printf("time_label: %%p=%p\n", time_label);
#endif
#ifdef D
    printf("[LINE:%d]", __LINE__);
    printf("Freeing 'temp'\n");
#endif
    //free(temp);

    return ret;

}//char *get_fname(char *fname) {
