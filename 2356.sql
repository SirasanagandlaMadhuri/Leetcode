Number of unique subjects taught by each teacher
# Write your MySQL query statement below
select teacher_id,Count(distinct subject_id) as cnt from Teacher group by teacher_id
