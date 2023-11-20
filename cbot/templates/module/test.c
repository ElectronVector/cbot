{# Used to generate the test file when creating a module. #}

#include "unity.h"

#include "{{ include_str }}"

void setUp(void)
{
}

void tearDown(void)
{
}

void test_{{ module_name }}_NeedToImplement(void)
{
    TEST_IGNORE_MESSAGE("Need to Implement {{ module_name }}");
}