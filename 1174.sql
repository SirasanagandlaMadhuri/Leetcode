
IMMEDIATE FOOD DELIVERY II
  
# Write your MySQL query statement below
select round(sum(d1.order_Date=d1.customer_pref_delivery_date)*100.0/count(*),2) as immediate_percentage from Delivery d1 left join Delivery d2
on d1.customer_id=d2.customer_id
and d1.order_date>d2.order_date
where d2.customer_id is null
