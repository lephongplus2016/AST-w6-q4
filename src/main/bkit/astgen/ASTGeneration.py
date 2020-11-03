from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *


class ASTGeneration(BKITVisitor):


    # def visitProgram(self, ctx: BKITParser.ProgramContext):
    #     return Program(ctx.vardecls().accept(self))

    # def visitVardecls(self, ctx: BKITParser.VardeclsContext):
    #     return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    # def visitVardecltail(self, ctx: BKITParser.VardecltailContext):
    #     if ctx.getChildCount() == 0: return []
    #     return ctx.vardecl().accept(self) + ctx.vardecltail().accept(self)

    # def visitVardecl(self, ctx: BKITParser.VardeclContext):
    #     return [VarDecl(x, ctx.mptype().accept(self)) for x in ctx.ids().accept(self)]

    # def visitMptype(self, ctx: BKITParser.MptypeContext):
    #     return IntType() if ctx.INTTYPE() else FloatType()

    # def visitIds(self, ctx: BKITParser.IdsContext):
    #     if ctx.getChildCount() > 1: return [Id(ctx.ID().getText())] + ctx.ids().accept(self)
    #     return [Id(ctx.ID().getText())]

    def visitProgram(self,ctx:BKITParser.ProgramContext):

        return Binary(ctx.exp().accept(self))

    def visitExp(self,ctx:BKITParser.ExpContext):
        if ctx.getChildCount() == 1:
            return ctx.term().accept(self)
        else:
            return ctx.term().accept(self) + ctx.exp().accept(self)

    def visitTerm(self,ctx:BKITParser.TermContext): 
        if ctx.getChildCount() == 1:
            return ctx.factor().accept(self)
        else:
            return ctx.factor().accept(self) + ctx.factor().accept(self)

    def visitFactor(self,ctx:BKITParser.FactorContext):
        if ctx.getChildCount() == 1:
            return ctx.operand().accept(self)
        else:
            return ctx.factor().accept(self) + ctx.operand().accept(self)

    def visitOperand(self,ctx:BKITParser.OperandContext):
        if ctx.ID():
            return [Id(ctx.ID().getText())] 
        elif ctx.INTLIT():
            return IntLiteral()
        elif ctx.BOOLIT():
            return BooleanLiteral()
        else: return Binary(ctx.exp().accept(self))