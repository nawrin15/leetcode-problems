---approach - 1
select *, IF(x + y > z and z + y > x and z + x > y, 'Yes', 'No') as triangle
from triangle

---approach - 2
select x, y, z, 
case when x + y > z and x + z > y and y + z > x then 'Yes'  
     else 'No'  
end as triangle
from Triangle