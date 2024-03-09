#편의점
cc_buy = 500
cc_sale=1800
sk_buy=900
sk_sale=1400
bm_buy=800
bm_sale=1800
ds_buy=3500
ds_sale=4000
co_buy=700
co_sale=1500
sa_buy=1000
sa_sale=2000

sk=0
sk=sk-(sk_buy*10)
bm=0
bm+=bm_sale*2
ds=0
ds-=ds_buy*5
ds+=ds_sale*4
co=0
co+=co_sale*1
sa=0
sa+=sa_sale*4
cc=0
cc+=cc_sale*5

total=sk+bm+ds+co+sa+cc
print(total)

