// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
    @8192   //8k
    D=A
    @R0
    M=D

(LOOP)
    @KBD
    D=M

    @i      // 进入循环前初始化i=0
    M=0
    @draw
    D;JNE   // 当按下键盘时，进入draw循环

    @i      // 进入循环前初始化i=0
    M=0
    @cls
    0;JMP   // 无条件清屏

    @LOOP   // 无限循环
    0;JMP

(draw)
	// for(i=0;i<8k;++i)
	//      mem[screen+i]=-1
    @i
    D=M
    @R0
    D=M-D
    @LOOP
    D;JEQ   // 屏幕全部填充为黑色，结束draw，继续LOOP的无限循环

    // mem[screen+i]=1, ++i
    @SCREEN
	D=A
	@i
	D=D+M
    A=D
    M=-1
    @i
    M=M+1
    
    @draw
    0;JMP


(cls)
	// for(i=0;i<8k;++i)
	//      mem[screen+i]=0
    @i
    D=M
    @R0
    D=M-D
    @LOOP
    D;JEQ       // 屏幕全部填充为白色，结束cls，继续LOOP的无限循环

    // mem[screen+i]=0, ++i
    @SCREEN
	D=A
	@i
	D=D+M
    A=D
    M=0
    @i
    M=M+1
    
    @cls
    0;JMP
