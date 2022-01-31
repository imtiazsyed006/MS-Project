classdef BNO055_block < matlab.System & coder.ExternalDependency
    %
    % System object template for a sink block.
    % 
    % This template includes most, but not all, possible properties,
    % attributes, and methods that you can implement for a System object in
    % Simulink.
    %
    % NOTE: When renaming the class name Sink, the file name and
    % constructor name must be updated to use the class name.
    %
    
    % Copyright 2016-2018 The MathWorks, Inc.
    %#codegen
    %#ok<*EMCA>
    
    properties
        % Public, tunable properties.
%         MW_I2C_SCD = 1;
        
    end
    
    properties (Nontunable)
        % Public, non-tunable properties.
    end
    
    properties (Access = private)
        % Pre-computed constants.
    end
    
    methods
        % Constructor
        function obj = BNO055_block(varargin)
            % Support name-value pair arguments when constructing the object.
            setProperties(obj,nargin,varargin{:});
            coder.allowpcode('plain');
        end
    end
    
    methods (Access=protected)
        function setupImpl(obj) %#ok<MANU>
            if isempty(coder.target)
                % Place simulation setup code here
            else
                % Call C-function implementing device initialization
                coder.cinclude('MW_c2000GPIO.h');
                coder.cinclude('MW_I2C.h','InAllSourceFiles',true);
                coder.cinclude('BNO055_driver.h');
%                 coder.ceval('MW_digitalIOPin_open',31,1);
%                 coder.ceval('MW_digitalIOPin_open',34,1)
                coder.ceval('sleepAbit');
                coder.ceval('MW_I2C_Open',0,0);
                coder.ceval('Dontwait');
                coder.ceval('WhyWait');
            end
        end
        
        function [A_x, A_y, A_z, M_x, M_y, M_z, G_x, G_y, G_z] = stepImpl(~)  %#ok<INUSD>
            out = zeros(1,9);
            if isempty(coder.target)
                % Place simulation output code here 
            else
                % Call C-function implementing device output
%                 coder.ceval('MW_digitalIOPin_write',31,u);
%                 coder.ceval('MW_digitalIOPin_write',34,u);
                  coder.ceval('HitIt',coder.wref(out));
                  A_x = out(1);
                  A_y = out(2);
                  A_z = out(3);
                  M_x = out(4);
                  M_y = out(5);
                  M_z = out(6);
                  G_x = out(7);
                  G_y = out(8);
                  G_z = out(9);
            end
        end
        
        function releaseImpl(obj) %#ok<MANU>
            if isempty(coder.target)
                % Place simulation termination code here
            else
                % Call C-function implementing device termination
                %coder.ceval('sink_terminate');
            end
        end
    end
    
    methods (Access=protected)
        %% Define input properties
        function num = getNumInputsImpl(~)
            num = 0;
        end
        
        function num = getNumOutputsImpl(~)
            num = 9;
        end
        
        function flag = isInputSizeMutableImpl(~,~)
            flag = false;
        end
        
        function flag = isInputComplexityMutableImpl(~,~)
            flag = false;
        end
        
        function validateInputsImpl(~)
            if isempty(coder.target)
                % Run input validation only in Simulation
%                 validateattributes(u,{'double'},{'scalar'},'','u');
            end
        end
        
        function icon = getIconImpl(~)
            % Define a string as the icon for the System block in Simulink.
            icon = 'BNO055';
        end
    end
    
    methods (Static, Access=protected)
        function simMode = getSimulateUsingImpl(~)
            simMode = 'Interpreted execution';
        end
        
        function isVisible = showSimulateUsingImpl
            isVisible = false;
        end
    end
    
    methods (Static)
        function name = getDescriptiveName()
            name = 'BNO055';
        end
        
        function b = isSupportedContext(context)
            b = context.isCodeGenTarget('rtw');
        end
        
        function updateBuildInfo(buildInfo, context)
            if context.isCodeGenTarget('rtw')
                % Update buildInfo
                srcDir = fullfile(matlabshared.supportpkg.getSupportPackageRoot,'toolbox','target','supportpackages','tic2000','src'); %#ok<NASGU>
                includeDir = fullfile(matlabshared.supportpkg.getSupportPackageRoot,'toolbox','target','supportpackages','tic2000','inc');

                srcDir_1 = fullfile(matlabshared.supportpkg.getSupportPackageRoot,'toolbox','target','shared','svd','src'); %#ok<NASGU>
                includeDir_1 = fullfile(matlabshared.supportpkg.getSupportPackageRoot,'toolbox','target','shared','svd','include');

                srcDir_2 = fullfile(fileparts(mfilename('fullpath')),'src'); %#ok<NASGU>
                includeDir_2 = fullfile(fileparts(mfilename('fullpath')),'include');

                addIncludePaths(buildInfo,includeDir);
                addIncludePaths(buildInfo,includeDir_1);
                addIncludePaths(buildInfo,includeDir_2);

                % Use the following API's to add include files, sources and
                % linker flags
                addIncludeFiles(buildInfo,'MW_I2C.h',includeDir_1);
                addSourceFiles(buildInfo,'MW_c2000GPIO.c',srcDir);
                addSourceFiles(buildInfo,'MW_I2C.c',srcDir);
                addSourceFiles(buildInfo,'BNO055_driver.c',srcDir_2);
                %addLinkFlags(buildInfo,{'-lSource'});
                %addLinkObjects(buildInfo,'sourcelib.a',srcDir);
                %addCompileFlags(buildInfo,{'-D_DEBUG=1'});
%                 addDefines(buildInfo,'MW_I2C_SCD')
            end
        end
    end
end
