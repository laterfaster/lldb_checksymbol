import lldb 

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand('command script add -f checksymbol.CheckSymbol checksymbol')

def CheckSymbol(debugger, command, result, internal_dict):
    res = lldb.SBCommandReturnObject()
    interpreter = debugger.GetCommandInterpreter()
    target = debugger.GetSelectedTarget()
    paras = command.split(' ')
    if len(paras) != 2:
            print('need 2 para, address length')
            return
    addr = paras[0]
    _len = paras[1]
    expression = 'x/{}xb {}'.format(_len, addr)
    interpreter.HandleCommand(expression, res)
    if res.HasResult():
        raw_out = res.GetOutput()
        for line in raw_out.split('\n'):
                if not line:
                    continue
                one_line = line.split(' ')
                addr_detail = one_line[0]
                # 由于小端模式，将数据倒序
                symbol_addr = '0x' + ''.join([i.replace('0x', '') for i in one_line[-1:0:-1]])
                # lldb内部函数，查找地址对应的符号
                symbol_detail = lldb.SBCommandReturnObject()
                interpreter.HandleCommand('im loo -a ' + symbol_addr,symbol_detail)
                # 将数据输出到lldb控制台
                if symbol_detail.HasResult():
                    sdetail = symbol_detail.GetOutput()
                    adetail = lldb.SBCommandReturnObject()
                    interpreter.HandleCommand('im loo -a ' + addr_detail[0:-1],adetail)
                    if adetail.HasResult():
                        sadetail = adetail.GetOutput()
                        print(addr_detail, '<' +sadetail.split('\n')[1][14::], '>','\t', symbol_addr, '\t',sdetail.split('\n')[1][14::])