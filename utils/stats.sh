#!/usr/bin/bash

TIME_FORMAT='{"command_ran":"%C","real_time_spent":%e,"main_memory_swaps":%W,"cpu_metrics":{"cpu_time_in_userspace":%U,"cpu_time_in_kernelspace":%S,"cpu_percentage_received":"%P"},"memory_metrics":{"average_shared_text":%X,"average_unshared_data":%D,"average_unshared_stack":%p,"average_total_usage":%K,"average_residental_memory":%t,"max_residental_memory":%M},"io_metrics":{"filesystem_inputs":%I,"filesystem_output":%O,"socket_messages_received":%r,"socket_messages_sent":%s},"page_faults":{"major":%F,"minor":%R},"context_switching":{"involuntarily":%c,"voluntarily":%w}}'

/usr/bin/time -f "${TIME_FORMAT}" -o time.json "$@"

jq -r '.' time.json > time_formatted.json && rm time.json
