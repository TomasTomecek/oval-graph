import json

from .client import Client


class ClientJsonInput(Client):
    def __init__(self, args):
        super().__init__(args)
        self.json_data_file = self.get_json_data_file()

    def get_only_fail_rule(self, rules):
        """
        Function processes array of matched IDs of rules in selected file.
        Function retunes array of failed matched IDs of rules in selected file.
        """
        raise NotImplementedError

    def _get_rows_of_unselected_rules(self):
        """
        Function retunes array of rows where is not selected IDs of rules in selected file.
        """
        raise NotImplementedError

    def get_json_data_file(self):
        with open(self.source_filename, 'r') as file_:
            try:
                return json.load(file_)
            except Exception:
                raise ValueError(
                    'Used file "{}" is not valid json.'.format(
                        self.source_filename))

    def search_rules_id(self):
        rules = self._get_wanted_rules(
            self.json_data_file.keys())
        notselected_rules = []
        return self._check_rules_id(rules, notselected_rules)
