<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>AirDrive</title>
    <!-- Tailwind CSS CDN for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Configure Tailwind to use Inter font and extend colors if needed -->
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        inter: ['Inter', 'sans-serif'],
                        roboto: ['Roboto', 'sans-serif'] // Keeping Roboto as it was in original
                    }
                }
            }
        }
    </script>

    <!-- Fonts Start - Using Inter now, keeping Roboto as a fallback/alternative -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@100..900&family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap"
        rel="stylesheet" />
    <!-- Fonts End -->
</head>

<!-- Applying Inter font globally and a light grey background -->
<body class="font-inter bg-gray-100 min-h-screen flex">
    <!-- Mobile Menu Toggle Button -->
    <!-- Positioned absolutely, hidden on large screens (md:hidden) -->
    <button class="fixed top-4 left-4 z-50 p-2 bg-white rounded-lg shadow-md md:hidden" id="mobile-menu-toggle">
        <!-- Hamburger icon using SVG -->
        <svg class="w-6 h-6 text-gray-700" viewBox="0 0 24 24">
            <path fill="currentColor" d="M3 18h18v-2H3v2zm0-5h18v-2H3v2zm0-7v2h18V6H3z" />
        </svg>
    </button>

    <!-- Main Container for Sidebar and Content -->
    <div class="flex flex-1">
        <!-- Sidebar Start -->
        <!-- Responsive: Fixed position, full height, hidden on small screens by default (hidden md:flex) -->
        <!-- Uses 'translate-x-full' for off-screen and 'translate-x-0' for on-screen in JS -->
        <div class="sidebar fixed top-0 left-0 w-64 h-full bg-white shadow-lg p-4 z-40 transition-transform duration-300 ease-in-out -translate-x-full md:translate-x-0 md:relative md:flex md:flex-col" id="sidebar">
            <div class="sidebar-header flex items-center mb-6">
                <!-- Google Drive icon using direct URL for simplicity -->
                <img src="https://ssl.gstatic.com/images/branding/product/1x/drive_2020q4_48dp.png" alt="AirDrive Logo" class="w-8 h-8 mr-2" />
                <span class="text-xl font-semibold text-gray-800">AirDrive</span>
            </div>

            <!-- New Button for file/folder actions -->
            <button id="new-button" class="new-button bg-blue-600 text-white py-2 px-4 rounded-lg shadow-md hover:bg-blue-700 transition duration-200 flex items-center justify-center mb-4">
                <!-- Plus icon as inline SVG -->
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
                </svg>
                New
            </button>

            <!-- New Upload Dropdown Menu -->
            <!-- Initially hidden, shown via JavaScript -->
            <div id="new-upload" class="new-upload absolute top-28 left-4 bg-white border border-gray-200 rounded-lg shadow-xl py-2 w-48 z-50 hidden">
                <input id="new-upload-focus" type="text"
                    class="h-0 w-0 border-none absolute -z-10" readonly aria-hidden="true" />
                <!-- New Folder Button -->
                <div id="new-folder-btn" class="flex items-center px-4 py-2 hover:bg-gray-100 cursor-pointer text-gray-700">
                    <!-- Folder icon as inline SVG -->
                    <svg class="w-5 h-5 mr-3 text-yellow-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"></path>
                    </svg>
                    New Folder
                </div>
                <hr class="my-1 border-gray-200" />
                <!-- File Upload Button -->
                <div id="file-upload-btn" class="flex items-center px-4 py-2 hover:bg-gray-100 cursor-pointer text-gray-700">
                    <!-- Upload icon as inline SVG -->
                    <svg class="w-5 h-5 mr-3 text-indigo-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0113 3.414L16.586 7A2 2 0 0118 8.414V16a2 2 0 01-2 2H4a2 2 0 01-2-2V4zm2 6a1 1 0 011-1h6a1 1 0 110 2H7a1 1 0 01-1-1zm1 3a1 1 0 100 2h6a1 1 0 100-2H7z" clip-rule="evenodd"></path>
                    </svg>
                    File Upload
                </div>
                <!-- Hidden file input for actual file selection -->
                <input type="file" id="fileInput" class="h-0 w-0 border-none absolute -z-10" aria-hidden="true" />
                <hr class="my-1 border-gray-200" />
                <!-- URL Upload Button -->
                <div id="url-upload-btn" class="flex items-center px-4 py-2 hover:bg-gray-100 cursor-pointer text-gray-700">
                    <!-- Link icon as inline SVG -->
                    <svg class="w-5 h-5 mr-3 text-teal-500" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                    </svg>
                    URL Upload
                </div>
            </div>

            <!-- Sidebar Navigation Menu -->
            <div class="sidebar-menu mt-6 flex flex-col space-y-2">
                <a class="selected-item flex items-center px-4 py-2 rounded-lg bg-blue-100 text-blue-800 font-medium" href="/?path=/">
                    <!-- Home icon as inline SVG -->
                    <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path>
                    </svg>
                    Home
                </a>
                <a class="unselected-item flex items-center px-4 py-2 rounded-lg text-gray-700 hover:bg-gray-100 transition duration-200" href="/?path=/trash">
                    <!-- Trash icon as inline SVG -->
                    <svg class="w-5 h-5 mr-3" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 011-1h4a1 1 0 110 2H8a1 1 0 01-1-1zm-1 3a1 1 0 100 2h8a1 1 0 100-2H6z" clip-rule="evenodd"></path>
                    </svg>
                    Trash
                </a>
            </div>
        </div>
        <!-- Sidebar End -->

        <!-- Background Blur for Modals - Initially hidden -->
        <div id="bg-blur" class="bg-blur fixed inset-0 bg-black bg-opacity-50 z-30 hidden"></div>

        <!-- Create New Folder Modal -->
        <!-- Hidden by default, shown via JavaScript -->
        <div id="create-new-folder" class="create-new-folder fixed inset-0 flex items-center justify-center z-50 hidden">
            <div class="bg-white p-6 rounded-lg shadow-xl w-96 max-w-sm flex flex-col space-y-4">
                <span class="text-xl font-semibold text-gray-800">New Folder</span>
                <input type="text" id="new-folder-name" placeholder="Enter Folder Name" autocomplete="off"
                    class="p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 outline-none" />
                <div class="flex justify-end space-x-3 mt-4">
                    <button id="new-folder-cancel" class="py-2 px-4 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition duration-200">Cancel</button>
                    <button id="new-folder-create" class="py-2 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">Create</button>
                </div>
            </div>
        </div>
        <!-- Create New Folder End -->

        <!-- File / Folder Rename Modal -->
        <!-- Hidden by default, shown via JavaScript -->
        <div id="rename-file-folder" class="create-new-folder fixed inset-0 flex items-center justify-center z-50 hidden">
            <div class="bg-white p-6 rounded-lg shadow-xl w-96 max-w-sm flex flex-col space-y-4">
                <span class="text-xl font-semibold text-gray-800">Edit File/Folder Name</span>
                <input type="text" id="rename-name" placeholder="Enter New Name" autocomplete="off"
                    class="p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 outline-none" />
                <div class="flex justify-end space-x-3 mt-4">
                    <button id="rename-cancel" class="py-2 px-4 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition duration-200">Cancel</button>
                    <button id="rename-create" class="py-2 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">Rename</button>
                </div>
            </div>
        </div>
        <!-- File / Folder Rename End -->

        <!-- Move/Copy Modal Start -->
        <!-- Hidden by default, shown via JavaScript -->
        <div id="move-copy-modal" class="create-new-folder fixed inset-0 flex items-center justify-center z-50 hidden">
            <div class="bg-white p-6 rounded-lg shadow-xl w-96 max-w-sm flex flex-col space-y-4">
                <span id="move-copy-title" class="text-xl font-semibold text-gray-800">Move Item</span>
                <div class="folder-tree max-h-64 overflow-y-auto border border-gray-200 rounded-md p-2 bg-gray-50" id="folder-tree">
                    <!-- Folder tree will be populated here by JavaScript -->
                    <p class="text-gray-500 text-sm">Loading folders...</p>
                </div>
                <div class="move-copy-actions flex justify-end space-x-3 mt-4">
                    <button id="move-copy-cancel" class="py-2 px-4 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition duration-200">Cancel</button>
                    <button id="move-item-btn" class="primary-btn py-2 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">Move</button>
                    <button id="copy-item-btn" class="secondary-btn py-2 px-4 bg-gray-700 text-white rounded-lg hover:bg-gray-800 transition duration-200">Copy</button>
                </div>
            </div>
        </div>
        <!-- Move/Copy Modal End -->

        <!-- Remote Upload Modal -->
        <!-- Hidden by default, shown via JavaScript -->
        <div id="new-url-upload" class="create-new-folder fixed inset-0 flex items-center justify-center z-50 hidden">
            <div class="bg-white p-6 rounded-lg shadow-xl w-96 max-w-sm flex flex-col space-y-4">
                <span class="text-xl font-semibold text-gray-800">URL Upload</span>
                <input type="text" id="remote-url" placeholder="Enter Direct Download Link Of File" autocomplete="off"
                    class="p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 outline-none" />
                <div id="single-threaded-div" class="flex items-center space-x-2 text-gray-700">
                    <input type="checkbox" name="single-threaded-toggle" id="single-threaded-toggle" class="form-checkbox h-4 w-4 text-blue-600 rounded" />
                    <label for="single-threaded-toggle" class="text-sm">Single Threaded</label>
                    <a href="#" class="text-blue-500 hover:text-blue-700" title="Info about single-threaded download">
                        <!-- Info icon as inline SVG -->
                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zm-2 2a1 1 0 00-1 1v3a1 1 0 102 0V9a1 1 0 00-1-1z" clip-rule="evenodd"></path>
                        </svg>
                    </a>
                </div>
                <div class="flex justify-end space-x-3 mt-4">
                    <button id="remote-cancel" class="py-2 px-4 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition duration-200">Cancel</button>
                    <button id="remote-start" class="py-2 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">Upload</button>
                </div>
            </div>
        </div>
        <!-- Remote Upload End -->

        <!-- Get Password Modal (Admin Login) -->
        <!-- Hidden by default, shown via JavaScript -->
        <div id="get-password" class="create-new-folder fixed inset-0 flex items-center justify-center z-50 hidden">
            <div class="bg-white p-6 rounded-lg shadow-xl w-96 max-w-sm flex flex-col space-y-4">
                <span class="text-xl font-semibold text-gray-800">Admin Login</span>
                <input type="password" id="auth-pass" placeholder="Enter Password" autocomplete="off"
                    class="p-2 border border-gray-300 rounded-md focus:ring-blue-500 focus:border-blue-500 outline-none" />
                <div class="flex justify-end mt-4">
                    <button id="pass-login" class="py-2 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition duration-200">Login</button>
                </div>
            </div>
        </div>
        <!-- Get Password End -->

        <!-- File Uploader Status Modal -->
        <!-- Hidden by default, shown via JavaScript -->
        <div id="file-uploader" class="file-uploader fixed inset-0 flex items-center justify-center z-50 hidden">
            <div class="bg-white p-6 rounded-lg shadow-xl w-96 max-w-sm flex flex-col space-y-3">
                <span class="upload-head text-lg font-semibold text-gray-800 flex items-center">
                    <!-- Rocket emoji for visual flair -->
                    <span class="mr-2 text-2xl">🚀</span> Uploading File...
                </span>
                <span id="upload-filename" class="upload-info text-gray-700">Filename: <span class="font-medium">N/A</span></span>
                <span id="upload-filesize" class="upload-info text-gray-700">Filesize: <span class="font-medium">N/A</span></span>
                <span id="upload-status" class="upload-info text-gray-700">Status: <span class="font-medium">Initializing...</span></span>
                <span id="upload-percent" class="upload-info text-gray-700">Progress: <span class="font-medium">0%</span></span>
                <div class="progress w-full bg-gray-200 rounded-full h-3 mt-2">
                    <div class="progress-bar bg-blue-500 h-full rounded-full transition-all duration-300 ease-out" id="progress-bar" style="width: 0%;"></div>
                </div>
                <div class="btn-div flex justify-end mt-4">
                    <button id="cancel-file-upload" class="py-2 px-4 bg-red-500 text-white rounded-lg hover:bg-red-600 transition duration-200">Cancel Upload</button>
                </div>
            </div>
        </div>
        <!-- File Uploader End -->

        <!-- Main Content Area -->
        <!-- Adjusted margin for sidebar on large screens (md:ml-64) -->
        <div class="main-content flex-1 p-6 md:ml-64 transition-all duration-300 ease-in-out">
            <div class="header flex flex-col md:flex-row justify-between items-start md:items-center mb-6 space-y-4 md:space-y-0">
                <!-- Search Bar -->
                <div class="search-bar flex items-center bg-white rounded-full px-4 py-2 shadow-sm flex-grow md:max-w-md w-full">
                    <!-- Search icon as inline SVG -->
                    <svg class="w-5 h-5 text-gray-500 mr-2" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd" d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" clip-rule="evenodd"></path>
                    </svg>
                    <form id="search-form" class="flex-grow">
                        <input id="file-search" type="text" placeholder="Search in Drive" autocomplete="off"
                            class="w-full bg-transparent outline-none text-gray-800 placeholder-gray-500" />
                    </form>
                </div>
                
                <!-- Sort Controls -->
                <div class="sort-controls flex items-center space-x-3 mt-4 md:mt-0">
                    <select id="sort-by" class="sort-select p-2 border border-gray-300 rounded-md bg-white text-gray-700 focus:ring-blue-500 focus:border-blue-500 outline-none">
                        <option value="date">Sort by Date</option>
                        <option value="name">Sort by Name</option>
                        <option value="size">Sort by Size</option>
                    </select>
                    <button id="sort-order" class="sort-order-btn p-2 bg-white border border-gray-300 rounded-md shadow-sm text-gray-700 hover:bg-gray-100 transition duration-200" data-order="desc" title="Toggle Sort Order">
                        <!-- Sort order icon (up/down arrow) -->
                        <svg class="w-4 h-4 text-gray-600" viewBox="0 0 24 24" width="16" height="16">
                            <path fill="currentColor" d="M7 14l5-5 5 5z"/>
                        </svg>
                    </button>
                </div>
            </div>

            <!-- Breadcrumb Navigation -->
            <div class="breadcrumb-container bg-white p-3 rounded-lg shadow-sm mb-6 overflow-x-auto whitespace-nowrap">
                <div class="breadcrumb flex items-center space-x-2 text-gray-600" id="breadcrumb">
                    <!-- Breadcrumb will be populated here by JavaScript -->
                    <span class="text-gray-400">Home</span>
                </div>
            </div>

            <!-- Directory Table -->
            <div class="directory bg-white rounded-lg shadow overflow-hidden">
                <div class="table-wrapper overflow-x-auto">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Name</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">File Size</th>
                                <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">More</th>
                            </tr>
                        </thead>
                        <tbody id="directory-data" class="bg-white divide-y divide-gray-200">
                            <!-- Directory data will be populated here by JavaScript -->
                            <tr>
                                <td colspan="3" class="px-6 py-4 whitespace-nowrap text-sm text-gray-500 text-center">No files or folders found.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
           
