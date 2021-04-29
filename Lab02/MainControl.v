module MainControl(
	input [5:0] Opcode,
	
	output reg RegDst, RegWrite, ALUSrc,
	output reg MemtoReg, MemRead, MemWrite,
	output reg Branch,
	output reg [1:0] ALUOp);
	
	always @(*) begin
		case(Opcode)
			0: begin  /* Tipo R */
				RegDst 		<= 1;
				ALUSrc 		<= 0;
				MemtoReg	<= 0;
				RegWrite	<= 1;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= 2'b10;
			end
			35: begin /* LW */
				RegDst 		<= 0;
				ALUSrc 		<= 1;
				MemtoReg	<= 1;
				RegWrite	<= 1;
				MemRead		<= 1;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= 2'b00;
			end
			43: begin /* SW */
				RegDst 		<= 0;
				ALUSrc 		<= 1;
				MemtoReg	<= 0;
				RegWrite	<= 0;
				MemRead		<= 0;
				MemWrite	<= 1;
				Branch		<= 0;
				ALUOp		<= 2'b00;
			end
			4: begin /* BEQ */
				RegDst 		<= 0;
				ALUSrc 		<= 0;
				MemtoReg	<= 0;
				RegWrite	<= 0;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 1;
				ALUOp		<= 2'b01;
			end
			3: begin /* JAL */
				RegDst 		<= 2'd2; ###
				ALUSrc 		<= x;
				MemtoReg	<= 0;
				RegWrite	<= 1;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= x;
			end
			5: begin /* BNE */
				RegDst 		<= 0;
				ALUSrc 		<= 1;
				MemtoReg	<= 0;
				RegWrite	<= 0;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= 2'b01;
			end
			8: begin /* ADDI */
				RegDst 		<= 0;
				ALUSrc 		<= 1;
				MemtoReg	<= 0;
				RegWrite	<= 1;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= 2'b00;
			end
			12: begin /* ANDI */
				RegDst 		<= 0;
				ALUSrc 		<= 1;
				MemtoReg	<= 0;
				RegWrite	<= 1;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= 2'b10;
			end
			13: begin /* ORI */
				RegDst 		<= 0;
				ALUSrc 		<= 1;
				MemtoReg	<= 0;
				RegWrite	<= 1;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= 3'b100; ###
			end
			14: begin /* XORI */
				RegDst 		<= 0;
				ALUSrc 		<= 1;
				MemtoReg	<= 0;
				RegWrite	<= 1;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= 3'b101; ###
			end
			1: begin /* BGEZ E BGEZAL */
				ALUSrc 		<= 1;
				MemtoReg	<= 0;
				MemRead		<= 0;
				MemWrite	<= 0;
				Branch		<= 0;
				ALUOp		<= 3'b111;

				if(bgez) begin
					RegDst 		<= 0;
					RegWrite	<= 0;
				end
				else begin
					RegDst 		<= 2'd2; #####
					RegWrite	<= 1;
				end
			end
		endcase
	end
endmodule