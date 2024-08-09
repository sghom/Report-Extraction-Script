import os
import shutil

path = r'R:\kirby_group\External Group Data\UHN_Soroush\Reports'
destination_root = r'Z:\ra\uhn\Reports'
subject_paths = [os.path.join(path, subject) for subject in os.listdir(path) if os.path.isdir(os.path.join(path, subject))]

for subject_path in subject_paths:
    report_id = os.listdir(subject_path)[0]
    report_path = os.path.join(subject_path, report_id)
    subject_name = os.path.basename(subject_path)
    destination_subject_folder = os.path.join(destination_root, subject_name, report_id)
    
    if not os.path.exists(destination_subject_folder):
        os.makedirs(destination_subject_folder)
    
    reports_source = os.path.join(report_path, 'reports')
    reports_destination = os.path.join(destination_subject_folder, 'reports')
    
    if os.path.exists(reports_source):
        shutil.copytree(reports_source, reports_destination)
