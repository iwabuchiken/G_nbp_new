	list	p=10f200
	#include <p10f200.inc>

;==== file info ==================
;@file_info@
;=================================

;==== configuration ==================
	__CONFIG	_CP_OFF & _WDT_OFF & _MCLRE_OFF & _IntRC_OSC

;==== variables ==================
CNT1	EQU		0x10
CNT2	EQU		0x11
CNT3	EQU		0x12

;==== setup ==================
	ORG		0x00

	movwf	OSCCAL
	bcf		OSCCAL,FOSC4

	movlw	b'11111110'
	TRIS	GPIO

;==== main_loop ==================
main_loop

	bsf		GPIO,0
	call	DLY_1S

	bcf		GPIO,0
	call	DLY_1S

	goto	main_loop

;==== delay module ==================
DLY_1S
	movlw	d'10'
	movwf	CNT3
DLY_100
	movlw	d'100'
	movwf	CNT1
DLP1
	movlw	d'200'
	movwf	CNT2
DLP2
	nop
	nop
	decfsz	CNT2,f
	goto	DLP2
	decfsz	CNT1,f
	goto	DLP1
	decfsz	CNT3,f
	goto	DLY_100

	retlw	0

;==== end ==================
	END
