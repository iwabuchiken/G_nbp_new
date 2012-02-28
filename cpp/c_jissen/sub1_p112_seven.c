/************************************`
 * <Basics>
 *	1. File: sub1_p112_seven.c
 *	2. Author: Iwabuchi Ken				*
 *	3. Date: 20120218_062001
 *	4. Dependencies:
 *		1) Header:	C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_07_work\exc_7-6\mylib1.h	v=1.1
 *		2) File:	C:\workspaces\ws_ubuntu_1\G20111104_083701_C_learn_01\C_jissen_work\Chp_07_work\exc_7-6\mylib1.c	v=1.1
 * <Aim>
 * 	1.
 * <Usage>
 *	1. Execute the program			*
 * <Source>
 * 	1. Oualline: 112
 * <Related>
 * 	1.
 * <Others>
 ************************************/

#ifndef INCLUDE_STDIO_H
#define INCLUDE_STDIO_H
#include <stdio.h>
#endif

#ifndef INCLUDE_STDIO_H
#define INCLUDE_STDIO_H /* exit() */
#include <stdlib.h>
#endif

#ifndef INCLUDE_STRING_H
#define INCLUDE_STRING_H
#include <string.h>
#endif
#ifndef INCLUDE_TIME_H
#define INCLUDE_TIME_H
#include <time.h>
#endif

#define show(dt, typ) \
			printf(#dt"=%"#typ"(%%"#typ")\n", dt)
#define show1(dt) \
			printf(#dt"\n")

#ifdef MYLIB1
#ifndef INCLUDE_MYLIB_1_H
#define INCLUDE_MYLIB_1_H
#include "mylib1.h"
#endif
#endif

// macros ============================

// global vars ============================
char	line[100];		/* input line	*/
int		seven_count;	/* number of 7 in the list	*/
int		data[5];		/* data list	*/
//int		data[6];		/* data list	*/
int		three_count;	/* number of 3 in the list	*/
int		index;			/* index for the list		*/
// prototypes ============================


// functions ============================

int main(int argc, char* argv[])
{
	/* variables	*/

	/* initialize	*/
	seven_count		= 0;
	three_count		= 0;

	/* processes
	 * 1. input data
	 * 2. process
	 * 3. show result
	 */

	/* 1. input data	*/
	printf("Enter 5 numbers\n");
	printf("\t(space between data)=> ");

		/* fgets() and sscanf()	*/
	fgets(line, sizeof(line), stdin);
	sscanf(line, "%d %d %d %d %d",
			&data[1], &data[2], &data[3],
			&data[4], &data[5]);

	/* 2. process data	*/
	for (index = 1; index <= 5; ++index) {
		//debug
		printf("[LINE:%d]", __LINE__);
		printf("Before: index=%d"
				" data[%d]=%d\n",
				index, index, data[index]);
		printf("\tthree_count=%d "
				"seven_count=%d\n",
				three_count, seven_count);

		if (data[index] == 3)
			++three_count;
		if (data[index] == 7)
			++seven_count;

		//debug
		printf("[LINE:%d]", __LINE__);
		printf("After: index=%d"
				" data[%d]=%d\n",
				index, index, data[index]);
		printf("\tthree_count=%d "
				"seven_count=%d\n",
				three_count, seven_count);
	}//for (index = 1; index <= 5; ++index)

	/* 3. show result	*/
	printf("Threes %d Sevens %d\n",
				three_count, seven_count);
	return (0);
}//int main(int argc, char* argv[])

/*
#ifdef D
    printf("[LINE:%d]", __LINE__);
#endif
*/
