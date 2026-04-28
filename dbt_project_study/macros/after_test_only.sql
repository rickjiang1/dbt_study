{% macro after_test_only(results) %}
  {% if flags.WHICH == 'test' %}
    -- run SQL here
    insert into dbo.dbt_test_audit(run_type)
    values ('after dbt test');
  {% endif %}
{% endmacro %}