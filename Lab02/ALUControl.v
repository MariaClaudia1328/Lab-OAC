module ALUControl (ALUOp, FuncCode, ALUCtl);

	input [1:0] ALUOp;
	input [5:0] FuncCode;
	output reg [3:0] ALUCtl;
	
	always @(ALUOp, FuncCode) begin
	if(ALUOp == 0)
		ALUCtl <= 2;    //LW and SW use add
	else if(ALUOp == 1)
		ALUCtl <= 6;	// branch BEQ use subtract
	else if (ALUOp == 6)   
		ALUCtl <= 0;    // AND
	else if (ALUOp == 3) 
		ALUCtl <= 12;   // NOR
	else if (ALUOp == 4)
		ALUCtl <= 1; 	//OR
	else if (ALUOp == 5)
		ALUCtl <= 13;	//XOR
	else if (ALUOp == 7)
		ALUCtl <= 8;	//Branch BGEZ/BGEZAL
	else if (ALUOp == 8)
		ALUCtl <= 3;	//ADDU
	else if (ALUOp == 9)
		ALUCtl <= 15;	//LUI
	else if (ALUOp == 2)
		case(FuncCode)
			32: ALUCtl <= 2; //add
			33: ALUCtl <= 3; //addu
			36: ALUCtl <= 0; //and	
			11: ALUCtl <= 8; //movn		
			39: ALUCtl <= 12; //nor
			37: ALUCtl <= 1; //or	
			42: ALUCtl <= 9; //slt
			34: ALUCtl <= 6; //sub		
			35: ALUCtl <= 7; //subu
			38: ALUCtl <= 13; //xor	
			default: ALUCtl <= 15; //should not happen
		endcase
	end
endmodule