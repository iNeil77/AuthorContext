require 'torch'
require 'lmdb'
require 'os'
require 'xlua'


db = lmdb.env{Path = './docDB', Name = 'docDB'}
db:open()
weight =torch.Tensor(6000, 100)

data = torch.data(weight)

row = (#weight)[1]
print(row)
txn = db:txn()

xlua.progress(1, row)
cur = 1

for i = 1, row do

    tensor = torch.Tensor(100)
    for j = 1, 100 do
        tensor[j] = data[cur]
        cur = cur + 1
    end
    txn:put(i, tensor)

    if i % 1000 == 0 then
        collectgarbage()
        txn:commit()
        txn = db:txn()
        xlua.progress(i, row)
    end
end    
print(cur)
xlua.progress(row, row)

txn:put('num_docs', row)
txn:commit()
db:close()


