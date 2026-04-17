{% test testing_relationship(model, column_name,field,to) %}

with parent as (

    select
        {{ field }} as parent_id

    from {{ to }}

),

child as (

    select
        {{column_name}} as child_id

    from {{model}}

)

select *
from child
where child_id is not null
and child_id not in (select parent_id from parent)

{% endtest %}