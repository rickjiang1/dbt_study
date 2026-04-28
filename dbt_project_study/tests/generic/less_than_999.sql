{% test less_than_999(model, column_name) %}

{{ config(severity = 'error') }}

with validation as (

    select
        {{ column_name }} as even_field

    from {{ model }}

),

validation_errors as (

    select
        even_field

    from validation
    where even_field > 999

)

select *
from validation_errors

{% endtest %}