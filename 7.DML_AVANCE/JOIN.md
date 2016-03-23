
### Facturation

Imprimer le nom et le montant de la facture totale des personnes habitant la ville de Lubumbashi

```
mysql> select m.last_name as Nom, sum(p.amount) as Facture from customer m, address a, city c, rental r , payment p where p.rental_id = r.rental_id and r.customer_id = m.customer_id and m.address_id = a.address_id and a.city_id = c.city_id and city like 'Lubumbashi' group by m.last_name;
```
