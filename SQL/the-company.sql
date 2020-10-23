select c.company_code, c.founder, count(distinct lm.lead_manager_code),
    count(distinct sm.senior_manager_code), count(distinct m.manager_code),
    count(distinct e.employee_code)


from Company c, Lead_Manager lm, Senior_Manager sm, Manager m, Employee e
where c.company_code = lm.company_code
    and lm.lead_manager_code = sm.lead_manager_code
    and sm.senior_manager_code = m.senior_manager_code
    and m.manager_code = e.manager_code
group by c.company_code, c.founder
order by c.company_code