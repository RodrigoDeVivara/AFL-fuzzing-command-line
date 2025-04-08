#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sillypare.h"
#include "hardcore_northcutt.h"

extern list_type get_lexem_list(status *program_status);
extern cmd_link build_syntax_tree(list_type lst,int start_index,int end_index);
extern void rm_syntax_tree(cmd_link tree);
extern int get_lexem_list_len(list_type lst);
extern void run_tree(cmd_link tree);

int main(int argc, char *argv[]) {
    status program_status = Success;
    char input[4096];

    if (fgets(input, sizeof(input), stdin) == NULL)
        return 1;

    FILE *tmp = fmemopen(input, strlen(input), "r");
    if (!tmp) return 1;
    FILE *old_stdin = stdin;
    stdin = tmp;

    list_type lexems = get_lexem_list(&program_status);
    if (program_status != Success) {
        fclose(tmp);
        stdin = old_stdin;
        return 1;
    }

    int len = get_lexem_list_len(lexems);
    cmd_link tree = build_syntax_tree(lexems, 0, len - 1);
    run_tree(tree);
    rm_syntax_tree(tree);

    fclose(tmp);
    stdin = old_stdin;
    return 0;
}
