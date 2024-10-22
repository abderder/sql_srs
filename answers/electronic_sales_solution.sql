select category, sum(price)
from sales
group by category