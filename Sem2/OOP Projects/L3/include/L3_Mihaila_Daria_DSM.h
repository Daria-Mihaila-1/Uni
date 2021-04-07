#include <vector>
#include <string>
using namespace std;

class DSM
{
    private:
    int el_count;
    int** matrix;
    vector<string> names;

    void resize();

    public:
    
    DSM(vector <string> element_names);
    
    DSM(int elementcount);

    DSM(const DSM& obj);

    ~DSM();

    int size();

    void set_element_name(int index, string name);

    string get_name(int index);

    void add_link(string from_element, string to_element, int weight);

    void delete_link(string from_element, string to_element);

    bool have_link(string from_element, string to_link);

    int link_weight(string   from_element,   string to_link);
    
    int count_to_links(string element);

    int count_from_links(string element);

    int count_all_links();

    double calculate_matrix_density();
};