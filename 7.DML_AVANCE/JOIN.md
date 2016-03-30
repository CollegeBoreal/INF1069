
### Facturation

Imprimer le nom et le montant de la facture totale des personnes habitant la ville de Lubumbashi

```
mysql> select m.last_name as Nom, sum(p.amount) as Facture 
from customer m, address a, city c, payment p 
where 
    p.customer_id = m.customer_id 
and m.address_id = a.address_id 
and a.city_id = c.city_id 
and city like 'Lubumbashi' group by m.last_name;
```


Imprimer le nom et le montant de la facture totale des personnes habitant le Congo (ANSI-92)

```
select o.country as Pays, m.last_name as Nom, sum(p.amount) as Facture from 
customer m
inner join address a on m.address_id = a.address_id
inner join city c on a.city_id = c.city_id 
inner join country o on o.country_id = c.country_id 
inner join payment p on p.customer_id = m.customer_id 
where country like 'Congo%' or country like 'Algeria' group by o.country, m.last_name having sum(p.amount) > 100;
```
