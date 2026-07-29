/* Auto-generated Hardware-Software Interface Header for UART0 */
#ifndef UART0_H
#define UART0_H

#include <stdint.h>

/* Base Address */
#define UART0_BASE_ADDR (0x40001000UL)

/* --- CTRL: Control register --- */
#define UART0_CTRL_OFFSET (0x00)
#define UART0_CTRL_ADDR (UART0_BASE_ADDR + UART0_CTRL_OFFSET)

#define UART0_CTRL_TXEN_POS (0)
#define UART0_CTRL_TXEN_MASK (0x00000001UL)
#define UART0_CTRL_ENABLE_POS (1)
#define UART0_CTRL_ENABLE_MASK (0x00000002UL)

#endif /* UART0_H */