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

char * get_fname( char *fname_in ) {
#ifdef D
printf("[LINE:%d] \n", __LINE__);
printf("=================== Entering 'get_fname' ===================\n");
#endif
    char *time_label = NULL;
    char *fname_out = calloc(strlen(fname_in)+20,
                            sizeof(char));
    time_label = get_time_label();
    sprintf(fname_out, "%s_%s.pgm", fname_in, time_label);
#ifdef D
printf("=======================================\n");
printf("[LINE:%d] \n", __LINE__);
printf("time_label = get_time_label()\n");
printf("time_label: %%s=%s %%p=%p &=%p\n",
            time_label, time_label, time_label);
printf("fname_in: %%s=%s %%p=%p &=%p\n",
            fname_in, fname_in, fname_in);
printf("fname_out: %%s=%s %%p=%p &=%p\n",
            fname_out, fname_out, fname_out);
printf("=======================================\n");
#endif

    free(time_label);
#ifdef D
printf("=======================================\n");
printf("[LINE:%d] \n", __LINE__);
printf("<<time_label freed>>\n");
printf("time_label = get_time_label()\n");
printf("time_label: %%s=%s %%p=%p &=%p\n",
            time_label, time_label, time_label);
printf("fname_in: %%s=%s %%p=%p &=%p\n",
            fname_in, fname_in, fname_in);
printf("fname_out: %%s=%s %%p=%p &=%p\n",
            fname_out, fname_out, fname_out);
printf("=======================================\n");
#endif

#ifdef D
printf("[LINE:%d] \n", __LINE__);
printf("=================== Exiting 'get_fname' ===================\n");
#endif
    return fname_out;

}//char * get_fname( char *fname_in ) {

char * get_time_label( void )
{
#ifdef D
printf("[LINE:%d] \n", __LINE__);
printf("=================== Entering 'get_time_label' ===================\n");
#endif

    time_t current;
    struct tm *local;
    char * label = NULL;
#ifdef D
printf("=======================================\n");
printf("[LINE:%d] \n", __LINE__);
printf("'label' declared\n");
printf("label: %%s=%s %%p=%p &=%p\n", label, label, label);
printf("=======================================\n");
#endif
    label = malloc(sizeof(char) * 20);
#ifdef D
printf("=======================================\n");
printf("[LINE:%d] \n", __LINE__);
printf("label mallocked\n");
printf("label: %%s=%s %%p=%p &=%p\n", label, label, label);
printf("=======================================\n");
#endif
    time(&current);
    local = localtime(&current);
    strftime(label, 255, "%Y%m%d_%H%M%S", local);
#ifdef D
printf("=======================================\n");
printf("[LINE:%d] \n", __LINE__);
printf("strftime done to 'label'\n");
printf("label: %%s=%s %%p=%p &=%p\n", label, label, label);
printf("=======================================\n");
#endif
#ifdef D
printf("[LINE:%d] \n", __LINE__);
printf("=================== Exiting 'get_time_label' ===================\n");
#endif
    return label;

}//char * get_time_label( void )

void show_fileinfo()
{
    printf("created at=%s\n", CREATED_AT);
    printf("modified at=%s\n", MODIFIED_AT);
    printf("file version=%s\n", FILE_VERSION);
}
